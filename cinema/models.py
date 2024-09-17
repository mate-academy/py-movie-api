from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=63)
    description = models.TextField(blank=True)
    duration = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.title} ({self.duration}) min long"
