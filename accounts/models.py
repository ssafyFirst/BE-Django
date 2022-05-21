from django.db import models
from django.contrib.auth.models import AbstractUser
from actors.models import Actor
from movies.models import Genre

# Create your models here.


class User(AbstractUser):
    img = models.ImageField(upload_to='accounts/', blank=True)
    like_actors = models.ManyToManyField(Actor, related_name='like_users')
    like_genres = models.ManyToManyField(Genre, related_name='like_users')