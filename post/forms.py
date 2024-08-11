from django import forms
from .models import Post


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "description", "author"]
        # exclude = ["created_at", "updated_at"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form__field"}),
            "description": forms.TextInput(attrs={"class": "form__field"}),
            "author": forms.TextInput(attrs={"class": "form__field"})
        }
