from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=63)
    description = models.TextField(
        max_length=512,
        null=True,
        blank=True
    )
    duration = models.PositiveIntegerField()

    class Meta:
        verbose_name_plural = "movies"

    def __str__(self):
        return f"Movie: {self.title} (id = {self.id})"
