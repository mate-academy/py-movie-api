from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=63)
    description = models.TextField(blank=True, null=True)
    duration = models.DurationField(blank=True)

    def __str__(self):
        return self.title
