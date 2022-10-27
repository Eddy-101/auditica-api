from django.db import models

from apps.songs.models import Song

# Create your models here.
class Album(models.Model):
    name = models.CharField(max_length=100)
    songs = models.ManyToManyField(Song)
    thumbnail  = models.ImageField(upload_to="albums", null=True)
    description = models.TextField(blank=True)
