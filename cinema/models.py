from django.db import models
from django.core.validators import MinValueValidator

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=500, blank=True)
    duration = models.IntegerField(
        validators=[MinValueValidator(1)],
        help_text="Duration in minutes"
    )

    def __str__(self):
        return self.title
