from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.PositiveIntegerField()

    class Meta:
        verbose_name_plural = "Movies"

    def __str__(self):
        return (f"Movie: {self.title},"
                f" Duration: {self.duration},"
                f" Description: {self.description}"
                )
