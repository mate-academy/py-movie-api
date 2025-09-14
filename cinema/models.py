from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    duration = models.IntegerField(null=True, blank=True, default=0)

    class Meta:
        verbose_name_plural = "Movies"
        verbose_name = "Movie"

    def __str__(self):
        return self.title
