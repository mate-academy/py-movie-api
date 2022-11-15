from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=1024)
    duration = models.IntegerField()
