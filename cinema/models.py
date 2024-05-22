from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=127)
    description = models.TextField(blank=True)
    duration = models.PositiveIntegerField()

    def __str__(self):
        return f"Movie: {self.title}"
