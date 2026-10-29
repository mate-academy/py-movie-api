from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(blank=True, null=True)
    duration = models.IntegerField()
