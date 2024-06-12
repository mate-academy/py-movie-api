from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=124, unique=True)
    description = models.TextField(blank=True)
    duration = models.IntegerField()

    class Meta:
        verbose_name_plural = "movies"

    def __str__(self):
        return str(self.title)
