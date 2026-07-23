from django.db import models


class Movie(models.Model):
    title = models.CharField(
        max_length=255,
        unique=True,
    )
    description = models.TextField()
    duration = models.PositiveIntegerField()

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return f"Movie: {self.title} ({self.duration} min) - {self.description}"
