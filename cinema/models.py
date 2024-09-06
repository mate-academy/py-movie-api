from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.PositiveIntegerField()

    class Meta:
        verbose_name_plural = "movies"

    def __str__(self):
        return f"Movie title: {self.title}, id = {self.id}"
