from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    duration = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(300)]
    )

    class Meta:
        verbose_name_plural = "movies"
