from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255)
    duration = models.IntegerField()
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.title} ({self.duration} minutes)"
