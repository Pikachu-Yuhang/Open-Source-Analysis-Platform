from django.urls import path

from . import views

urlpatterns = [
    path('<str:owner>/<str:repo>/overview/', views.overview),
]