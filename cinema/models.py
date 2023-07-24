from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.DurationField()

    class Meta:
        verbose_name_plural = "movies"

    def __str__(self):
        return str(self.title)
