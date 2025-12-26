from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.PositiveIntegerField()

    def __str__(self) -> str:
        return (
            f"{self.title}: "
            f"{self.description[15:]}... "
            f"{self.duration}m"
        )
