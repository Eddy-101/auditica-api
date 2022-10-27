from django.db import models

from .managers import CategoryManager

# Create your models here.
class Category(models.Model):
    type = models.CharField(max_length=50)
    thumbnail = models.ImageField(upload_to="categories")
    description = models.TextField(null=True, blank=True)

    objects = CategoryManager()

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return f"{self.id} - {self.type}"