from django.db import models


class Movie(models.Model):
    title: str = models.CharField(max_length=255)
    description: str = models.CharField(max_length=255)
    duration: int = models.IntegerField()

    def __str__(self) -> str:
        return self.title
