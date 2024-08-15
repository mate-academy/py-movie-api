from django.db import models

from django.contrib.auth.models import AbstractUser


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    duration = models.IntegerField()

    def __str__(self):
        return self.title


class Director(AbstractUser):
    pass
