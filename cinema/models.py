from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(default="")
    duration = models.IntegerField()

    class Meta:
        ordering = ["title"]
