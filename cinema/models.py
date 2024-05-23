from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    duration = models.IntegerField()

    def __str__(self) -> str:
        return (
            f"Movie: {self.id}, "
            f"{self.title}, "
            f"{self.description}, "
            f"{self.duration}"
        )
