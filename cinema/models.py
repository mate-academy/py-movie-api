from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.title} is {self.duration} minutes long"
