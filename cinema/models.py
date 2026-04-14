from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.IntegerField(help_text="Duration in minutes")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["id"]
