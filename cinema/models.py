from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.IntegerField()

    def __str__(self):
        return (f"Film: {self.title},"
                f" duration: {self.duration},"
                f" description: {self.description}")
