from django.db import models

# Create your models here.
# models.py
from django.db import models


class AudioFile(models.Model):
    audio_file = models.FileField(upload_to='audio_temp/')
