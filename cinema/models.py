from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=133)
    description = models.CharField(max_length=255)
    duration = models.IntegerField()
