from django.urls import path

from . import views

urlpatterns = [
    path('<str:owner>/<str:repo>/info/<str:result_type>', views.info),
    path('<str:owner>/<str:repo>/update/', views.update),
]