from django.db import models

from apps.users.models import User
from apps.songs.models import Song

# Create your models here.
class FavoriteSongs(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="favorites")
    songs = models.ManyToManyField(Song)
