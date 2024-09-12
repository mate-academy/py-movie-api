from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=64, unique=True)
    description = models.TextField()
    duration = models.IntegerField()

    class Meta:
        ordering = ["title"]

    def __str__(self) -> str:
        return self.title
