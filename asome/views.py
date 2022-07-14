from django.shortcuts import render, get_object_or_404

from asome.models import Topic, User


def index(request):
    ctx = {
        "topics": Topic.objects.all(),
        "recently_joined_users": User.objects.order_by("-date")[:5]
    }
    return render(request, "asome/index.html", ctx)


def topic(request, topic_name):
    topic = get_object_or_404(Topic, name=topic_name)
    ctx = {
        "topic": topic,
    }
    return render(request, "asome/topic.html", ctx)


def user(request, username):
    user = get_object_or_404(User, name=username)
    ctx = {
        "user": user,
    }
    return render(request, "asome/user.html", ctx)
