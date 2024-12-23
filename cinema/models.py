from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=127)
    description = models.TextField(max_length=255)
    duration =models.IntegerField()

    class Meta:
        verbose_name_plural = "Movies"

    def __str__(self):
        return f"Movie: {self.title} (id = {self.id})"
