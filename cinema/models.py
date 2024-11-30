from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=1000, blank=True)
    duration = models.PositiveIntegerField()

    def __str__(self) -> str:
        return f"{self.title}"
