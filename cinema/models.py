from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField()
    duration = models.IntegerField()

    class Meta:
        verbose_name_plural = "movie"

    def __str__(self):
        return f"Title: {self.title}, duration: {self.duration}"
