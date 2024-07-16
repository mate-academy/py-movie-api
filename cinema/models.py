from django.core.validators import MinValueValidator
from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    duration = models.IntegerField(validators=[MinValueValidator(1)])

    class Meta:
        ordering = ["title"]

    def __str__(self) -> str:
        return self.title
