from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255, blank=True, default="")
    duration = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = "movies"

    def __str__(self):
        return self.title
