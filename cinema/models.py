from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=500, null=True, blank=True)
    duration = models.PositiveSmallIntegerField()

    class Meta:
        verbose_name_plural = "movies"

    def __str__(self):
        return f"Movie Title: {self.title} (id = {self.id})"
