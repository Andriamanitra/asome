from django.urls import path
from . import views

app_name = "asome"

urlpatterns = [
    path("", views.index, name="index"),
    path("t", views.add_topic, name="add_topic"),
    path("t/<str:topic_name>", views.topic, name="topic"),
    path("t/<str:topic_name>/like", views.like_topic, name="like_topic"),
    path("t/<str:topic_name>/dislike", views.dislike_topic, name="dislike_topic"),
    path("t/<str:topic_name>/comment", views.post_comment, name="post_comment"),
    path("u/<str:username>", views.user, name="user"),
    path("register", views.register, name="register"),
]
