from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=100, unique=True, blank=False)
    description = models.CharField(max_length=255, blank=True, null=True)
    duration = models.IntegerField(blank=False)

    def __str__(self):
        return self.title
