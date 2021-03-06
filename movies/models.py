from django.db import models
from django.conf import settings
from actors.models import Actor



class Genre(models.Model):
    name = models.CharField(max_length=50)


class Movie(models.Model):
    title = models.CharField(max_length=100)
    popularity = models.FloatField()
    poster_path = models.CharField(max_length=200)
    backdrop_path = models.CharField(max_length=200, null=True)
    genres = models.ManyToManyField(Genre, related_name='movie', blank=True)
    original_language = models.CharField(max_length=30, null=True)
    released_date = models.DateField()
    vote_average = models.FloatField()
    vote_count = models.IntegerField()
    overview = models.TextField()
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')
    actor1 = models.IntegerField(null=True)
    actor2 = models.IntegerField(null=True)
    actor3 = models.IntegerField(null=True)
    

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='comments')
    content = models.CharField(max_length=200)
    updated_at = models.DateTimeField(auto_now=True)