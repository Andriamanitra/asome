from django.urls import path
from . import views

app_name = "asome"

urlpatterns = [
    path("", views.index, name="index"),
    path("t/<str:topic_name>", views.topic, name="topic"),
    path("u/<str:username>", views.user, name="user"),
]
