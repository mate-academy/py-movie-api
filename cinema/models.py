from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=101)
    description = models.TextField(null=True, blank=True)
    duration = models.PositiveIntegerField()

    def __str__(self) -> str:
        return (f"{self.title} "
                f"(description: {self.description}, duration: {self.duration})")
