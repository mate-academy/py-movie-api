from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.IntegerField()

    def __str__(self):
        return (f"Movie name: {self.title}\n "
                f"Description: {self.description}\n "
                f"Duration time: {self.duration} minutes")
