from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=50)


class Movie(models.Model):
    adult = models.BooleanField(default=False)

    backdrop_path = models.CharField(max_length=200)
    original_language = models.CharField(max_length=30)
    original_title = models.CharField(max_length=50)
    overview = models.TextField()
    popularity = models.FloatField()
    poster_path = models.CharField(max_length=200)

    release_date = models.DateField()
    
    title = models.CharField(max_length=100)
    video = models.BooleanField()
    vote_average = models.FloatField()
    vote_count = models.IntegerField()
