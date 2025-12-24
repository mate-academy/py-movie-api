from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.PositiveIntegerField()

    class Meta:
        indexes = [models.Index(fields=["title"])]

    def __str__(self):
        return f"{self.title} - {self.duration}min"
