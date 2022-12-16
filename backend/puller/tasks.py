import datetime
import gzip, json, threading, os, queue, shutil
from urllib import request
from celery import shared_task

from puller.models import Actor, Batch, Event, Repo

class Puller:
    class AppURLopener(request.FancyURLopener):
        version = "Wget/1.21.2"

    def __init__(self, max_retry_cnt=100):
        self.max_retry_cnt = max_retry_cnt

    def get_actor(actor_json):
        actor = None
        try:
            actor = Actor.objects.get(pk=actor_json["id"])
        except:
            actor = Actor(
                id = actor_json["id"],
                url = actor_json["url"]
            )
            actor.save()
        return actor

    def get_repo(repo_json):
        repo = None
        try:
            repo = Repo.objects.get(pk=repo_json["id"])
        except:
            repo = Repo(
                id = repo_json["id"],
                full_name = repo_json["name"],
                url = repo_json["url"]
            )
            repo.save()
        return repo

    def json2model(event):
        e = Event(
            id = event["id"],
            full_type = event["type"],
            actor = Puller.get_actor(event["actor"]),
            repo = Puller.get_repo(event["repo"]),
            created_at = event["created_at"]
        )
        payload = event["payload"]
        match e.full_type:
            case 'ForkEvent':
                e.type = Event.EventType.Fork
            case 'IssueCommentEvent':
                match payload["action"]:
                    case 'created':
                        e.action = Event.Action.Commented
                    case other:
                        return None
                e.additional_info = payload["issue"]["id"]
                e.type = Event.EventType.Issue
            case 'IssuesEvent':
                match payload["action"]:
                    case 'opened':
                        e.action = Event.Action.Opened
                    case 'closed':
                        e.action = Event.Action.Closed
                    case other:
                        return None
                e.additional_info = payload["issue"]["id"]
                e.type = Event.EventType.Issue
            case 'MemberEvent':
                match payload["action"]:
                    case 'added':
                        e.action = Event.Action.Added
                    case 'removed':
                        e.action = Event.Action.Removed
                    case other:
                        return None
                e.type = Event.EventType.Member
            case 'PullRequestEvent':
                match payload["action"]:
                    case 'opened':
                        e.action = Event.Action.Opened
                    case 'closed':
                        e.action = Event.Action.Closed
                    case other:
                        return None
                e.additional_info = payload["pull_request"]["id"]
                e.type = Event.EventType.PullRequest
            case 'PullRequestReviewEvent':
                match payload["action"]:
                    case 'submitted':
                        e.action = Event.Action.Reviewed
                    case other:
                        return None
                e.additional_info = payload["pull_request"]["id"]
                e.type = Event.EventType.PullRequest
            case 'PullRequestReviewCommentEvent':
                match payload["action"]:
                    case 'created':
                        e.action = Event.Action.Commented
                    case other:
                        return None
                e.additional_info = payload["pull_request"]["id"]
                e.type = Event.EventType.PullRequest
            case 'PushEvent':
                e.additional_info = payload["size"]
                e.type = Event.EventType.Push
            case 'WatchEvent':
                e.type = Event.EventType.Watch
            case other:
                return None
        return e

    def producer(self, date, failure_list, q):
        opener = Puller.AppURLopener()
        for h in range(0, 24):
            f_name = f"{date.year}-{str(date.month).zfill(2)}-{str(date.day).zfill(2)}-{h}.json"
            gz_name = f"{f_name}.gz"

            retrieved, cnt = False, 0
            while not retrieved and cnt < self.max_retry_cnt:
                try:
                    opener.retrieve(f"https://data.gharchive.org/{gz_name}", gz_name)
                    retrieved = True
                except:
                    cnt += 1
            if retrieved:
                q.put(f_name)
            else:
                failure_list.append(f_name)

    def consumer(self, repo_paths, event_list, q):
        while True:
            f_name = q.get()
            if not f_name:
                q.task_done()
                break
            gz_name = f"{f_name}.gz"
            with gzip.open(gz_name, 'rb') as f_in, open(f_name, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
            os.remove(gz_name)
            with open(f_name, mode="r", encoding="utf-8") as f_in:
                event_json = ""
                for line in f_in:
                    event_json += line
                    try:
                        event = json.loads(event_json)
                        if event["repo"]["name"] in repo_paths:
                            e = Puller.json2model(event)
                            if e is not None:
                                event_list.append(e)
                        event_json = ""
                    except:
                        pass
            os.remove(f_name)
            q.task_done()

    def pull_event_data(self, batch_id, from_date, to_date):
        batch = Batch.objects.get(pk=batch_id)
        repo_paths = json.loads(batch.repo_paths)
        intervals = json.loads(batch.time_intervals)
        intervals.append([str(from_date), str(from_date)])

        date = from_date

        q, event_list = queue.Queue(), []
        consumers = [threading.Thread(target=self.consumer, args=(repo_paths, event_list, q)) for i in range(6)]
        for thread in consumers: thread.start()
        
        while date < to_date:
            failure_list = []

            producer = threading.Thread(target=self.producer, args=(date, failure_list, q))
            producer.start()
            producer.join()

            if len(failure_list) > 0:
                print(failure_list)
                break
            else:
                q.join()
                print(f"{date} done: {len(event_list)} events")
                Event.objects.bulk_create(event_list)
                event_list.clear()
                date += datetime.timedelta(days=1)
                intervals[-1][-1] = str(date)
                batch.time_intervals = json.dumps(intervals)
                batch.save()
        for thread in consumers:
            q.put("")
        q.join()
        for thread in consumers:
            thread.join()


def check_conflict(repo_paths):
    # TODO
    return True


def create_batch(repo_paths):
    batch_id = None
    if check_conflict(repo_paths):
        batch = Batch(
            repo_paths = json.dumps(repo_paths),
            time_intervals = json.dumps([])
        )
        batch.save()
        batch_id = batch.id
    return batch_id


@shared_task
def pull_data(batch_id, from_date, to_date):
    puller = Puller()
    puller.pull_event_data(batch_id, from_date, to_date)