from django.db import models


class Movie(models.Model):
    title = models.CharField()
    description = models.TextField(null=True)
    duration = models.PositiveSmallIntegerField()

    class Meta:
        verbose_name_plural = "movies"

    def __str__(self) -> str:
        return f"{self.title}"
