from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.IntegerField()

    class Meta:
        verbose_name_plural = "Movies"
        ordering = ("title",)

    def __str__(self):
        return self.title
