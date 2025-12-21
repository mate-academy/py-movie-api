from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(blank=True, null=True, max_length=500)
    duration = models.IntegerField()

    def __str__(self):
        return f"Movie name: {self.title}, duration: {self.duration}"

    class Meta:
        ordering = ["title"]
