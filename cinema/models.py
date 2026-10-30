from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True)
    duration = models.IntegerField()

    class Meta:
        verbose_name_plural = "cinema"

    def __str__(self) -> str:
        return f"Movie: {self.title} (id = {self.id})"
