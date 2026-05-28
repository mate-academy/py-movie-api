from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField()
    duration = models.IntegerField()

    def __str__(self) -> str:
        return self.title
