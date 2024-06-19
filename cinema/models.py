from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.IntegerField()

    class Meta:
        ordering = [
            "title",
        ]
