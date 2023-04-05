from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=127)
    description = models.TextField(null=True)
    duration = models.PositiveSmallIntegerField()

    def __str__(self) -> str:
        return str(self.title)
