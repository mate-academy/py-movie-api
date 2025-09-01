from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True)
    duration = models.PositiveIntegerField(help_text="Duration in minutes")

    def __str__(self):
        return self.title
