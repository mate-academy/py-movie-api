from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=255)
    duration = models.IntegerField()

    def __str__(self) -> str:
        return str(self.title)
