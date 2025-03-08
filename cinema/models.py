from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=False)
    duration = models.PositiveIntegerField(null=False)

    class Meta:
        verbose_name_plural = "Movies"

    def __str__(self):
        return f"{self.title}"
