from django.db import models
from .validators import len_min, author_name_valid


class Post(models.Model):
    title = models.CharField(verbose_name="title", max_length=64, validators=[len_min])
    description = models.TextField(verbose_name="description", max_length=1024, null=True, blank=True)
    author = models.CharField(verbose_name="author name", max_length=64, validators=[author_name_valid])

    img_field = models.ImageField(verbose_name="Image", upload_to='post-images/', null=True, blank=True)
    # post_id = models.PositiveIntegerField(primary_key=True, db_index=True)

    # First time it was created
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    # When it is edited!
    updated_at = models.DateTimeField(null=True, auto_now=True)
