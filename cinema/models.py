from django.db import models


class Movie(models.Model):

    title = models.CharField(max_length=200)
    description = models.TextField()
    duration = models.PositiveIntegerField()

    class Meta:
        verbose_name_plural = 'Movies'

    def __str__(self):
        return self.title
