from typing import Optional
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from asome.models import Topic, User, Comment
from asome.forms import UserForm, TopicForm


def index(request):
    ctx = {
        "topics": Topic.objects.all(),
        "recently_joined_users": User.objects.order_by("-date")[:5],
        "topic_form": TopicForm()
    }
    return render(request, "asome/index.html", ctx)


def topic(request, topic_name):
    topic = get_object_or_404(Topic, name=topic_name)
    ctx = {
        "topic": topic,
    }
    return render(request, "asome/topic.html", ctx)


def like_topic(request, topic_name):
    liked_topic = get_object_or_404(Topic, name=topic_name)
    user = valid_user(request)
    if user is None:
        return HttpResponse("Invalid user credentials", status=401)
    if user.likes.filter(pk=liked_topic.id).exists():
        user.likes.remove(liked_topic)
    else:
        user.likes.add(liked_topic)
    return topic(request, topic_name)


def dislike_topic(request, topic_name):
    disliked_topic = get_object_or_404(Topic, name=topic_name)
    user = valid_user(request)
    if user is None:
        return HttpResponse("Invalid user credentials", status=401)
    if user.dislikes.filter(pk=disliked_topic.id).exists():
        user.dislikes.remove(disliked_topic)
    else:
        user.dislikes.add(disliked_topic)
    return topic(request, topic_name)


def user(request, username):
    user = get_object_or_404(User, name=username)
    ctx = {
        "user": user,
    }
    return render(request, "asome/user.html", ctx)


def register(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            username = data["username"]
            secret = data["secret"]
            if User.objects.filter(name=username).exists():
                return HttpResponse("an user with that username already exists")
            new_user = User(name=username, secret=secret)
            new_user.save()
            ctx = {
                "user": new_user
            }
            return render(request, "asome/welcome.html", ctx)
        else:
            return HttpResponse("registration unsuccessful")
    ctx = {
        "form": UserForm()
    }
    return render(request, "asome/register.html", ctx)


def post_comment(request, topic_name):
    commented_topic = get_object_or_404(Topic, name=topic_name)
    user = valid_user(request)
    if user is None:
        return HttpResponse("Invalid user credentials", status=401)
    comment = Comment(topic=commented_topic, submitter=user, content=request.POST["content"])
    comment.save()
    return topic(request, topic_name)


def add_topic(request):
    if request.method != "POST":
        return HttpResponse("unsupported method (this end point only supports POST)")
    form = TopicForm(request.POST)
    if not form.is_valid():
        return HttpResponse("unlucky")
    topic_name = form.cleaned_data["name"]
    new_topic = Topic(name=topic_name)
    new_topic.save()
    return topic(request, topic_name)


def valid_user(request) -> Optional[User]:
    form = UserForm(request.POST)
    if not form.is_valid():
        return None
    data = form.cleaned_data
    username = data["username"]
    secret = data["secret"]
    try:
        return User.objects.get(name=username, secret=secret)
    except User.DoesNotExist:
        return None
