from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    duration = models.IntegerField()

    def __str__(self):
        return (f"Movie id: {self.id}, "
                f"title: {self.title}, "
                f"description: {self.description}, "
                f"duration: {self.duration}")
