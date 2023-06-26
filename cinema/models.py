from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=225)
    description = models.TextField(max_length=225)
    duration = models.TimeField(max_length=225)

    def __str__(self) -> str:
        return self.title
