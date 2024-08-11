from django.db import models
from .validators import len_min,author_name_valid


class Post(models.Model):
    title = models.CharField(max_length=64, validators=[len_min])
    description = models.TextField(max_length=1024, null=True)
    author = models.CharField(max_length=64, validators=[author_name_valid])

    # First time it was created
    created_at = models.DateTimeField(auto_now_add=True)

    # When it is edited!
    updated_at = models.DateTimeField(null=True, auto_now=True)
