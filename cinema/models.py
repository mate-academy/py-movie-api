from django.db import models


class Movie(models.Model):
    tittle = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    duration = models.IntegerField()

    class Mete:
        verbose_name_plural = "movies"

    def __str__(self):
        return self.tittle
