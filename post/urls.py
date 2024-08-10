from django.urls import path
from .views import home, create_post, delete

urlpatterns = [
    path('', home, name="home"),
    path('delete/<int:post_id>', delete, name="delete"),
    path('create/', create_post)
]
