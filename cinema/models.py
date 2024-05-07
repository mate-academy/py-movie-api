from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=50, null=False)
    description = models.TextField(max_length=500, null=False)
    duration = models.IntegerField()

    class Meta:
        verbose_name_plural = "movies"

    def __str__(self) -> str:
        return f"Title: {self.title}; Duration: {self.duration}"
