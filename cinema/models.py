from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    duration = models.IntegerField(null=True)
