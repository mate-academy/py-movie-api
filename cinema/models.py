from django.db import models
from django.db.models import CharField


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.IntegerField()

    def __str__(self) -> CharField:
        return self.title
