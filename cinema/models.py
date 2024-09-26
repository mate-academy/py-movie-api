from django.db import models
from django.core.validators import MinValueValidator


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.IntegerField(validators=[MinValueValidator(0)])

    def __str__(self):
        return f"Movie: {self.title}"
