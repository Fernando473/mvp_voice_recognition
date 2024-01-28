from django.urls import path
from .views import upload_audio, success_page, error_page, upload_audio_page

urlpatterns = [
    path('upload/', upload_audio, name='upload_audio'),
    path('success/', success_page, name='success_page'),
    path('error/', error_page, name='error_page'),
    path('upload_page/', upload_audio_page, name='upload_page')
]
