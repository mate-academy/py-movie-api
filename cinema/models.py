from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=73, unique=True)
    description = models.TextField(null=True, blank=True)
    duration = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.title}: ~ {self.duration} min."
