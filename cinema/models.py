from django.db import models


class Movie(models.Model):
    title: str = models.CharField(max_length=120)
    description: str = models.TextField()
    duration: int = models.IntegerField()

    class Meta:
        verbose_name_plural = "movies"
