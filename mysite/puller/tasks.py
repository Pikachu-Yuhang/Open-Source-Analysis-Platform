import concurrent.futures
import datetime
import gzip, json
from urllib import request
from celery import shared_task

from puller.models import Actor, Event, Repo, Watched

class Puller:
    class AppURLopener(request.FancyURLopener):
        version = "Wget/1.21.2"

    def __init__(self, limit=1000, max_retry=100):
        self.opener = Puller.AppURLopener()
        self.limit = limit
        self.max_retry = max_retry

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

    def get_watched_repos(repo_paths):
        repos = []
        for repo_path in repo_paths:
            repo = None
            try:
                repo = Watched.objects.get(pk=repo_path)
            except:
                repo = Watched(
                    repo_path = repo_path,
                    updated_till = datetime.date(2015, 1, 1)
                )
                repo.save()
            repos.append(repo)
        return repos

    def json2model(event):
        e = Event(
            event_type = Event.EventType[event["type"]],
            actor = Puller.get_actor(event["actor"]),
            repo = Puller.get_repo(event["repo"]),
            payload = event["payload"]
        )
        return e

    def pull_event_data(self, repo_paths, from_date, to_date=datetime.date.today()):
        events, date, success = [], from_date, True
        while date < to_date:
            for h in range(0, 23):
                f_name = f"{date.year}-{str(date.month).zfill(2)}-{str(date.day).zfill(2)}-{h}.json"
                url = f"https://data.gharchive.org/{f_name}.gz"

                response, retry_cnt = None, 0
                while response is None and retry_cnt < self.max_retry:
                    try:
                        response = self.opener.open(url)
                    except:
                        retry_cnt += 1
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
                            events.append(Puller.json2model(event))
                        event_json = ""
                    except:
                        pass
                print(f"{url} done")
            if not success:
                break
            else:
                print(f"{date} done: {len(events)} events")
                date += datetime.timedelta(days=1)
                if len(events) > self.limit:
                    break
        objs = []
        if success:
            objs = Event.objects.bulk_create(events)

            repos = Puller.get_watched_repos(repo_paths)
            for repo in repos:
                repo.updated_till = date
                repo.save()

        return date, objs


# def group_repos(repo_entries):
#     return [([repo], repo.updated_till) for repo in repo_entries]


# @shared_task
# def pull_data_beat():
#     all_entries = Watched.objects.all()
#     puller = Puller()

#     groups = group_repos(all_entries)
#     with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
#         futs = [executor.submit(puller.pull_event_data, [repo.repo_path for repo in repos], start) for (repos, start) in groups]
#         for fut in concurrent.futures.as_completed(futs):
#             pass


@shared_task
def pull_data(repo_paths, from_date=datetime.date(2015, 1, 1)):
    puller = Puller()
    date, end_date = from_date, datetime.date.today()
    while date < end_date:
        date, _ = puller.pull_event_data(repo_paths, from_date, end_date)
