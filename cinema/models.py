from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=60)
    description = models.CharField(max_length=250)
    duration = models.IntegerField()

    def __str__(self):
        return self.title
