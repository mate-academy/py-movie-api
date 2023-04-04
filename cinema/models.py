from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    duration = models.IntegerField()

    def __str__(self) -> str:
        return self.title
