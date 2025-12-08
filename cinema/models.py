from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255, null=False)
    description = models.TextField(null=False)
    duration = models.PositiveIntegerField(null=False)

    class Meta:
        verbose_name_plural = "movies"

    def __str__(self):
        return f"Title: {self.title} (duration: {self.duration})"
