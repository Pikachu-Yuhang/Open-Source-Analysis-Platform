import json
from django.http import HttpResponseNotFound, JsonResponse

from .models import SnapshotCache
from .tasks import fetcher

def pr_info(request, owner, repo):
    objs = SnapshotCache.objects.filter(repo_name=f"{owner}/{repo}", type=SnapshotCache.Type.PullRequest)
    if len(objs) > 0:
        result, res = objs[0].result, ''
        try:
            res = json.loads(objs[0].result)
        except:
            pass
        return JsonResponse({
            'result': res,
            'updated_at': objs[0].updated_at
        })
    else:
        return HttpResponseNotFound()


def issue_info(request, owner, repo):
    objs = SnapshotCache.objects.filter(repo_name=f"{owner}/{repo}", type=SnapshotCache.Type.Issue)
    if len(objs) > 0:
        result, res = objs[0].result, ''
        try:
            res = json.loads(objs[0].result)
        except:
            pass
        return JsonResponse({
            'result': res,
            'updated_at': objs[0].updated_at
        })
    else:
        return HttpResponseNotFound()


def other_info(request, owner, repo):
    objs = SnapshotCache.objects.filter(repo_name=f"{owner}/{repo}", type=SnapshotCache.Type.Other)
    if len(objs) > 0:
        result, res = objs[0].result, ''
        try:
            res = json.loads(objs[0].result)
        except:
            pass
        return JsonResponse({
            'result': res,
            'updated_at': objs[0].updated_at
        })
    else:
        return HttpResponseNotFound()