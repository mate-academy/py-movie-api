from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    duration = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = "movies"

    def __str__(self):
        return f"{self.title}: {self.description}. Duration: {self.duration}"
