from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import AbstractUser
from actors.models import Actor
from movies.models import Genre
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.core.validators import MinValueValidator

# Create your models here.


class User(AbstractUser):
    like_actors = models.ManyToManyField(Actor, related_name='like_users')
    like_genres = models.ManyToManyField(Genre, related_name='like_users')
    profile_img = ProcessedImageField(
        blank=True,
        upload_to='profile_img',
        processors=[ResizeToFill(300, 300)],
        format='JPEG',
        options={'quality': 70},
    )

    point = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0)],
    )

    def __str__(self):
        return self.username