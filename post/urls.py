from django.urls import path
from .views import home, create_post, delete, update
from config import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name="home"),
    path('delete/<int:post_id>', delete, name="delete"),
    path('update/<int:post_id>', update, name="update"),
    path('create/', create_post)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
