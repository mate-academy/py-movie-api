from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True)
    duration = models.IntegerField(null=True)
