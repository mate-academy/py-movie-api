from django.core.validators import (
    MinValueValidator,
    MaxValueValidator,
)
from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(null=True, max_length=255)
    duration = models.IntegerField(
        default=1,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(300),
        ],
    )

    def __str__(self):
        return f'Title: "{self.title}", Duration: {self.duration}'
