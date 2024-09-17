from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=255, null=True)
    duration = models.IntegerField()

    class Meta:
        verbose_name_plural = "movies"

    def __str__(self) -> str:
        return f"{self.title} {self.duration}"
