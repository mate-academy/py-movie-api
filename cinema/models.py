from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField()
    duration = models.IntegerField()

    class Meta:
        verbose_name = "Movie"
        verbose_name_plural = "Movies"

    def __str__(self):
        return f"Movie title: {self.title} (duration: {self.duration})"
