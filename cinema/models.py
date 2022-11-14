from django.db import models


class Movie(models.Model):
    title = models.TextField()
    description = models.CharField(max_length=255, blank=True, null=True)
    duration = models.IntegerField()
