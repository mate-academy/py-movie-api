from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(null=True, max_length=255)
    duration = models.IntegerField()
