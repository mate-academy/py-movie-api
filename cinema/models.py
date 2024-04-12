from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=255)
    duration = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.title}. Duration: {self.duration} minutes."
