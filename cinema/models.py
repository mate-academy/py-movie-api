from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255, null=False)
    description = models.TextField(null=False)
    duration = models.IntegerField(null=False)
