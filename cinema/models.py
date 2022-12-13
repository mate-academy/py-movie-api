from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=300)
    duration = models.IntegerField()

    def __str__(self):
        return str(self.title)
