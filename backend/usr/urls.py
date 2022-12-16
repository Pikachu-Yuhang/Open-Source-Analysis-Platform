from django.urls import path

from . import views

urlpatterns = [
    path('register/<str:usr_name>/<str:email>/<str:password>/', views.register),
    path('login/<str:usr_name>/<str:password>/', views.usr_login),
    path('logout/', views.usr_logout),
]