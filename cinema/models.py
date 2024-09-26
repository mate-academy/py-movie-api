from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=255)
    duration = models.IntegerField()

    def __str__(self) -> str:
        return f"ID {self.id} Title: {self.title}"
