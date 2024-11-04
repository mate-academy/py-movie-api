from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    duration = models.IntegerField()

    class Meta:
        verbose_name_plural = "movies"

    def __str__(self) -> str:
        return f"Movie: {self.title}(id: {self.id})"
