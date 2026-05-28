from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField()
    duration = models.IntegerField()

    def __str__(self):
        return f"Movie: {self.title} (id = {self.id})"
