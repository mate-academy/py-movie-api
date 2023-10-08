from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=63)
    description = models.CharField(max_length=63)
    duration = models.IntegerField()

    class Meta:
        verbose_name_plural = "movies"
        ordering = ["title"]
