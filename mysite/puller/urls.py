from django.urls import path

from . import views

urlpatterns = [
    path('<str:owner>/<str:repo>/pr_per_month/<int:year>/', views.pull_request_per_month),
    path('<str:owner>/<str:repo>/star_per_month/<int:year>/', views.star_per_month),
    path('<str:owner>/<str:repo>/commit_per_month/<int:year>/', views.commit_per_month),
    path('<str:owner>/<str:repo>/collaborator_per_month/<int:year>/', views.collaborator_per_month),
]