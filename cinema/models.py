from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=55)
    description = models.TextField()
    duration = models.IntegerField()
