"""Cinema database models."""
from __future__ import annotations
from django.core.validators import MinValueValidator
from django.db import models


class Movie(models.Model):
    """A film available through the API."""
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.PositiveIntegerField(validators=[MinValueValidator(1)])

    class Meta:
        """Model metadata."""
        ordering = ["id"]

    def __str__(self) -> str:
        """Return a readable movie label."""
        return self.title
