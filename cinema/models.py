from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=85)
    description = models.CharField(max_length=240)
    duration = models.IntegerField()
