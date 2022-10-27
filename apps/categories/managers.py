from django.db import models
from django.db.models import Count

class CategoryManager(models.Manager):
    def get_songs_category(self):
        songs = self.all()
        return songs

    def get_count_songs(self):
        songs = self.annotate(
            num_songs = Count('song')
        )

        return songs