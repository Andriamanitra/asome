import uuid
from django import forms


class UserForm(forms.Form):
    username = forms.CharField(label="Username", min_length=3, max_length=29)
    secret = forms.UUIDField(initial=uuid.uuid4, widget=forms.HiddenInput())


class TopicForm(forms.Form):
    name = forms.CharField(label="Suggest a new topic", max_length=97)
