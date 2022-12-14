from django.http import JsonResponse

from .models import Overview
from .tasks import fetcher

def overview(request, owner, repo):
    obj = None
    try:
        obj = Overview.objects.get(pk=f"{owner}/{repo}")
    except:
        obj = Overview(repo_name=f"{owner}/{repo}")
        fetcher.update_overview(obj)
        obj.save()
    return JsonResponse({
        'star_cnt': obj.star_cnt,
        'commit_cnt': obj.commit_cnt,
        'open_issue_cnt': obj.open_issue_cnt,
        'fork_cnt': obj.fork_cnt,
        'pr_creator_cnt': obj.pr_creator_cnt,
        'updated_at': obj.updated_at
    })