from django.contrib.auth.models import AbstractUser
from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    duration = models.PositiveIntegerField()

    class Meta:
        verbose_name_plural = "movies"

    def __str__(self) -> str:
        return f"Movie: {self.title}, duration: {self.duration} minutes"
