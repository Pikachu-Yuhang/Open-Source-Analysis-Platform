from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse

# Create your views here.
def register(request, usr_name, email, password):
    user = User.objects.create_user(usr_name, email, password)
    return HttpResponse("Success!")


def usr_login(request, usr_name, password):
    user = authenticate(request, username=usr_name, password=password)
    if user is not None:
        login(request, user)
        return HttpResponse("Success!")
    else:
        return HttpResponse("Failed!")


def usr_logout(request):
    logout(request)
    return HttpResponse("Success!")