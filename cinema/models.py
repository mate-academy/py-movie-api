from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    duration = models.IntegerField()

    class Meta:
        verbose_name_plural = "movies"

    def __str__(self):
        return (f"Tittle: {self.title},"
                f" Duration: {self.duration},"
                f" Description: {self.description}")
