from django.http import HttpResponse, JsonResponse

from .models import ResultCache
from .tasks import fetcher

def info(request, owner, repo, result_type):
    repo_name, type = f"{owner}/{repo}", ResultCache.Type[result_type]
    res, updated_time = fetcher.get_result_cache(repo_name, type)
    return JsonResponse({
        'result': res,
        'updated_time': updated_time
    })


def update(request, owner, repo):
    # TODO
    return HttpResponse("Update request receieved.")