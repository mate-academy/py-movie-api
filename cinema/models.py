from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255, blank=False)
    description = models.TextField()
    duration = models.PositiveIntegerField()

    def __str__(self):
        return self.title
