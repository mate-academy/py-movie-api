from django.core.validators import MinValueValidator
from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=31)
    description = models.TextField()
    duration = models.IntegerField(validators=[MinValueValidator(1)])
