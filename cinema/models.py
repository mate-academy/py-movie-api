from django.db import models


class Movie(models.Model):
    title = models.TextField(max_length=255, unique=True)
    description = models.TextField(max_length=255, blank=True, null=True)
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.title}, {self.duration} minutes"
