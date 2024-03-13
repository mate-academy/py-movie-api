from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    duration = models.PositiveIntegerField()

    def __str__(self) -> str:
        return f"{self.title} - {self.duration}"
