from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField(max_length=255)
    duration = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Movies'

    def __str__(self):
        return self.title
