from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255),
    description = models.TextField(max_length=255)
    duration = models.TimeField()

    def __str__(self):
        return f"{self.title}: {self.description}  (Time: {self.duration})"
