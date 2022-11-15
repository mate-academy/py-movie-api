from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=63)
    description = models.CharField(max_length=255, null=True, blank=True)
    duration = models.IntegerField()
