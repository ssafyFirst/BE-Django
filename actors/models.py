from django.db import models
from movies.models import Movie

# Create your models here.
class Actor(models.Model):
    name = models.CharField(max_length=30)
    profile_path = models.CharField(max_length=200)
    gender = models.IntegerField()
    # movies = models.ManyToManyField(Movie)
    