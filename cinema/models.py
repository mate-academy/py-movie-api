from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.IntegerField()

    def __str__(self) -> str:
        return (
            f"Title: {self.title}, "
            f"Description: {self.description}, "
            f"Duration{self.duration}"
        )
