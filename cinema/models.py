from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=70)
    description = models.TextField()
    duration = models.IntegerField()
