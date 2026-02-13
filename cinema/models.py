from django.contrib.auth.models import AbstractUser
from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=1000, null=True, blank=True)
    duration = models.IntegerField(default=90, null=True, blank=True)

    def __str__(self):
        return f"Title: {self.title} (id={self.id})"


class User(AbstractUser):
    pass
