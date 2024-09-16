from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=55)
    description = models.TextField(
        blank=True, default=""
    )
    duration = models.IntegerField()

    def __str__(self) -> str:
        return self.title
