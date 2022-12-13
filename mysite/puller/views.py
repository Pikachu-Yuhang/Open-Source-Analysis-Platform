from django.http import JsonResponse

from puller.models import Event, Repo

# Create your views here.
def pull_request_per_month(request, owner, repo, year):
    full_name = f"{owner}/{repo}"
    repo = Repo.objects.get(full_name=full_name)
    events = Event.objects.filter(created_at__year=year).filter(repo=repo).filter(type=Event.EventType.PullRequest)
    events_per_months = [events.filter(created_at__month=i+1) for i in range(0, 12)]
    opened = [events_in_month.filter(action=Event.Action.Opened).count() for events_in_month in events_per_months]
    closed = [events_in_month.filter(action=Event.Action.Closed).count() for events_in_month in events_per_months]
    return JsonResponse({'opened': opened, 'closed': closed})


def star_per_month(request, owner, repo, year):
    full_name = f"{owner}/{repo}"
    repo = Repo.objects.get(full_name=full_name)
    events = Event.objects.filter(created_at__year=year).filter(repo=repo).filter(type=Event.EventType.Watch)
    starred = [events.filter(created_at__month=i+1).count() for i in range(0, 12)]
    return JsonResponse({'starred': starred})