from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=55, null=True)
    description = models.CharField(max_length=255, null=True)
    duration = models.IntegerField()
