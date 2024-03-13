from django.contrib.auth.models import AbstractUser
from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    duration = models.DurationField()

    def __str__(self):
        return self.title


class User(AbstractUser):
    pass
