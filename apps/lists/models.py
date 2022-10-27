from django.db import models

from apps.songs.models import Song 
# Create your models here.
class ListSong(models.Model):
    songs = models.ManyToManyField(Song)
    thumbail = models.ImageField(upload_to="lists")
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)

    def __str__(self):
        return f'{self.id} - {self.name}'