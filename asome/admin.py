from django.contrib import admin

from .models import User, Topic, Comment

admin.site.register(User)
admin.site.register(Topic)
admin.site.register(Comment)
