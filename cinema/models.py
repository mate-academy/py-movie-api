from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField()
    duration = models.IntegerField()