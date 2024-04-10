from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=100, null=True)
    duration = models.IntegerField()

    def __str__(self):
        return self.title
