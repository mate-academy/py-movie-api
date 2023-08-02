from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    duration = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.title} - {self.duration} minutes"
