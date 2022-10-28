from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, default="")
    duration = models.IntegerField()

    def __str__(self) -> str:
        return str(self.title)
