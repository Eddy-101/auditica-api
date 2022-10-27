from django.db import models
from django.contrib.auth.models import AbstractBaseUser 
from django.contrib.auth.models import PermissionsMixin
from .managers import UserManager

from apps.albums.models import Album
from apps.lists.models import ListSong 
# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    image = models.ImageField(upload_to="users")
    lists = models.ManyToManyField(ListSong)
    is_staff = models.BooleanField(default=False)
    objects = UserManager()

    USERNAME_FIELD = 'email'

    class Meta():
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return f"{self.id}. {self.name} - {self.surname}"

    def name_complete(self):
        return f"{self.name} {self.surname}"

class Artist(User):
    description = models.TextField()
    album = models.ManyToManyField(Album) 
    cover = models.ImageField(upload_to="users/covers")
    
    class Meta():
        verbose_name = 'Artista'
        verbose_name_plural = 'Artistas'

    def __str__(self):
        return f"{self.id}. {self.name}"
