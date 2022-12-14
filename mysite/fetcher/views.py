from django.http import JsonResponse

from .tasks import fetcher

def overview(request, owner, repo):
    return JsonResponse(fetcher.overview(f"{owner}/{repo}"))