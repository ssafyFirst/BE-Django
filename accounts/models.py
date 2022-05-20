from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    img = models.ImageField(upload_to='accounts/', blank=True)