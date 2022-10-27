from django.db import models

from apps.categories.models import Category

# Create your models here.
class Song(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="songs")
    song = models.FileField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="song")
    reproductions = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'Musica'
        verbose_name_plural = 'Musicas'

    def __str__(self):
        return f"{self.id} - {self.name}"
