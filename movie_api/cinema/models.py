from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=10)
    description = models.TextField(max_length=50)
    duration = models.IntegerField()
