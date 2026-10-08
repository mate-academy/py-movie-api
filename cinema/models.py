from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=1000, null=True, blank=True)
    duration = models.IntegerField()
