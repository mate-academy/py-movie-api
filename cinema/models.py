from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    duration = models.CharField(max_length=10)

    def __str__(self):
        return f"Movie: {self.title}, {self.description}, {self.duration}"

    class Meta:
        ordering = ["title"]
        verbose_name = "movie"
        verbose_name_plural = "movies"
