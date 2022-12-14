from django.http import JsonResponse

from .models import SnapshotCache
from .tasks import fetcher

def overview(request, owner, repo):
    # TODO
    return JsonResponse({})