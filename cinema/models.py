from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    duration = models.PositiveIntegerField(help_text="Duration in minutes")

    class Meta:
        ordering = ["id"]

    def __str__(self) -> str:
        return f"{self.title} ({self.duration} min)"
