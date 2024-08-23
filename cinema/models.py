from __future__ import annotations

from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    duration = models.IntegerField()

    def __str__(self: Movie) -> str:
        return (f"Title: {self.title}, "
                f"Description: {self.description}, "
                f"Duration: {self.duration}")
