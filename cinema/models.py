from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=256, unique=True)
    description = models.TextField()
    duration = models.IntegerField()
