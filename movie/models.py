from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True)
    duration = models.PositiveSmallIntegerField()

    class Meta:
        verbose_name_plural = "movies"

    def __str__(self):
        return f"Cinema: {self.title} - {self.duration} (id={self.id})"
