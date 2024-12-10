from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    duration = models.PositiveIntegerField(help_text="Duration in minutes")

    def __str__(self):
        return self.title

    def formatted_duration(self):
        hours = self.duration // 60
        minutes = self.duration % 60
        return f"{hours}h {minutes}m"
