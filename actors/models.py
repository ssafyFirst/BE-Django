from django.db import models
from django.conf import settings

# Create your models here.
class Actor(models.Model):
    name = models.CharField(max_length=30)
    profile_path = models.CharField(max_length=200, null=True)
    gender = models.IntegerField()
    movie1 = models.IntegerField(null=True)
    movie2 = models.IntegerField(null=True)
    movie3 = models.IntegerField(null=True)
    
    
