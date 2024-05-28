from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.PositiveIntegerField()

    class Meta:
        verbose_name = "Movie"

    def __str__(self):
        return f"Movie: {self.title} (id = {self.id})"
