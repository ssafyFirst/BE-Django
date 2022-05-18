from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=50)


class Movie(models.Model):
    title = models.CharField(max_length=100)
    adult = models.BooleanField()
    popularity = models.FloatField()
    poster_path = models.CharField(max_length=200)
    backdrop_path = models.CharField(max_length=200, null=True)
    genres = models.ManyToManyField(Genre, related_name='movie', blank=True)
    original_language = models.CharField(max_length=30, null=True)
    released_date = models.DateField()
    vote_average = models.FloatField()
    vote_count = models.IntegerField()
    overview = models.TextField()
