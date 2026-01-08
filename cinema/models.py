from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=500, null=True)
    duration = models.PositiveIntegerField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Movies"
