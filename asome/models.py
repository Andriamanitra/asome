from django.db import models


class Topic(models.Model):
    name = models.CharField(max_length=97, unique=True)
    date = models.DateTimeField("date created", auto_now_add=True)

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=29, unique=True)
    secret = models.UUIDField()
    date = models.DateTimeField("date joined", auto_now_add=True)
    verified = models.BooleanField(default=False)
    likes = models.ManyToManyField(to=Topic, related_name="likes", blank=True)
    dislikes = models.ManyToManyField(to=Topic, related_name="dislikes", blank=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name="comments")
    submitter = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    date = models.DateTimeField("date submitted", auto_now_add=True)
    content = models.CharField(max_length=1024)

    def __str__(self):
        return f"Comment by {self.submitter} on {self.topic.name}"
