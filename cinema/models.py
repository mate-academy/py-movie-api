from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=100, blank=True, default="")
    description = models.TextField(blank=True, default="")
    duration = models.PositiveIntegerField()

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return f"{self.title} duration: {self.duration}"
