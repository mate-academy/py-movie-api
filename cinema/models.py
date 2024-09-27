from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=56)
    description = models.CharField(max_length=255, null=True, blank=True)
    duration = models.IntegerField()

    class Meta:
        verbose_name_plural = "cinemas"

    def __str__(self) -> str:
        return str(self.title)
