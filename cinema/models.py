from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.IntegerField()

    class Meta:
        ordering = ["id", "title"]
        verbose_name_plural = "Movies"

    def __str__(self):
        return self.title
