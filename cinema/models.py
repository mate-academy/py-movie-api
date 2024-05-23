from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True)
    duration = models.IntegerField()
