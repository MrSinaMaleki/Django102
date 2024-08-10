from django.urls import path
from .views import home, create_post

urlpatterns = [
    path('home/', home, name="home"),
    path('', create_post)
]
