import datetime
import gzip, json
from urllib import request
from celery import shared_task

from puller.models import Actor, Batch, Event, Repo

class Puller:
    class AppURLopener(request.FancyURLopener):
        version = "Wget/1.21.2"

    def __init__(self, max_retry_cnt=100):
        self.opener = Puller.AppURLopener()
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
        match e.type:
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

    def pull_event_data(self, batch_id, from_date, to_date):
        batch = Batch.objects.get(pk=batch_id)
        repo_paths = json.loads(batch.repo_paths)

        date, success = from_date, True
        while date < to_date and success:
            events = []
            for h in range(0, 24):
                f_name = f"{date.year}-{str(date.month).zfill(2)}-{str(date.day).zfill(2)}-{h}.json"
                url = f"https://data.gharchive.org/{f_name}.gz"

                response, cnt = None, 0
                while response is None and cnt < self.max_retry_cnt:
                    try:
                        response = self.opener.open(url)
                    except:
                        cnt += 1
                if response is None:
                    success = False
                    break
                result = gzip.decompress(response.read()).decode("utf-8")
                event_json = ""
                for line in result.splitlines():
                    event_json += line
                    try:
                        event = json.loads(event_json)
                        if event["repo"]["name"] in repo_paths:
                            e = Puller.json2model(event)
                            if e is not None:
                                events.append(e)
                        event_json = ""
                    except:
                        pass
                print(f"{url} done")
            if success:
                print(f"{date} done: {len(events)} events")
                Event.objects.bulk_create(events)
                date += datetime.timedelta(days=1)
        if from_date < date:
            intervals = json.loads(batch.time_intervals)
            intervals.append([str(from_date), str(date)])
            batch.time_intervals = json.dumps(intervals)
            batch.save()


def check_conflict(repo_paths):
    # TODO
    return True


def create_batch(repo_paths):
    id = None
    if check_conflict():
        batch = Batch(
            repo_paths = json.dumps(repo_paths),
            time_intervals = json.dumps([])
        )
        batch.save()
        id = batch.id
    return id


@shared_task
def pull_data(batch_id, from_date, to_date):
    puller = Puller()
    puller.pull_event_data(batch_id, from_date, to_date)