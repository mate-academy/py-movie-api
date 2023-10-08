from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    duration = models.PositiveSmallIntegerField(null=True)

    class Meta:
        ordering = ["title"]
        verbose_name_plural = "movies"

    def __str__(self) -> str:
        return str(self.title)
