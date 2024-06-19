from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True)
    duration = models.IntegerField()
