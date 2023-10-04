from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255, blank=False)
    description = models.TextField()
    duration = models.FloatField()

    class Meta:
        verbose_name_plural = "movies"

    def __str__(self):
        return str(self.title)
