from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255, blank=True, default='')
    description = models.TextField()
    duration = models.IntegerField()

