from django import forms
from .models import *


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"
        exclude = ["created_at", "updated_at"]
