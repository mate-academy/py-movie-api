from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    duration = models.IntegerField(help_text="in minutes")

    def __str__(self):
        return f"{self.title} ({self.duration} min)"
