from django.db import models


class Movie(models.Model):
    title = models.CharField(null=True, max_length=63)
    description = models.CharField(max_length=256)
    duration = models.IntegerField()

    class Meta:
        verbose_name_plural = "movies"

    def __str__(self):
        return str(self.title)
