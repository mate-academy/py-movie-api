from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=1000, blank=True)
    duration = models.IntegerField()
