from django.urls import path

from . import views

urlpatterns = [
    path('<str:owner>/<str:repo>/pr/', views.pr_info),
    path('<str:owner>/<str:repo>/issue/', views.issue_info),
    path('<str:owner>/<str:repo>/other/', views.other_info),
]