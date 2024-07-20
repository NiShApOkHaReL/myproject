from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.upload_image, name='upload_image'),
    path('display/', views.display_image, name='display_image'),
    path('view_parking_spaces/', views.view_parking_spaces, name='view_parking_spaces'),
    path('teams/', views.teams, name='teams'),
    path('upload/', views.upload_image, name='upload_image'),  # /upload/ URL

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)