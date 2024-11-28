from django.contrib.auth.models import AbstractUser
from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=80)
    description = models.CharField(max_length=250)
    duration = models.IntegerField()

    class Meta:
        verbose_name_plural = "movies"


class User(AbstractUser):
    pass
