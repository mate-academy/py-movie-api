from django.db import models


class Movie(models.Model):

    title = models.CharField(max_length=255)
    description = models.TextField(null=True)
    duration = models.IntegerField()

    def __str__(self):
        return str(self.title)
