from django.db import models


class Cinema(models.Model):
    title = models.CharField(max_length=63)
    description = models.TextField()
    duration = models.IntegerField()
