from django.urls import path
from .views import test,create_post

urlpatterns = [
    path('test/', test),
    path('', create_post)
]
