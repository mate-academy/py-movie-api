from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=500, null=True, blank=True)
    duration = models.IntegerField()

    def __str__(self):
        return f"Film - {self.title}, duration - {self.duration} minutes."
