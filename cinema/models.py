from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=512)
    duration = models.PositiveSmallIntegerField()

    def __str__(self) -> str:
        return self.title
