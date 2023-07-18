from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=55, null=True)
    description = models.CharField(max_length=255)
    duration = models.IntegerField()

    class Meta:
        verbose_name_plural = "movies"

    def __str__(self):
        return self.title
