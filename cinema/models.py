from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255, verbose_name="Film title")
    description = models.TextField(verbose_name="Film description")
    duration = models.IntegerField(verbose_name="Film duration (min)")

    class Meta:
        verbose_name_plural = "movies"

    def __str__(self):
        return f"{self.title} {self.description} ({self.description})"
