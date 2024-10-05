from django.db import models


class Movie(models.Model):
    title = models.CharField(unique=True, max_length=63)
    description = models.CharField(null=True, blank=True, max_length=255)
    duration = models.IntegerField()

    def __str__(self):
        return (f"title: {self.title}, "
                f"description: {self.description}, "
                f"duration: {self.duration}, "
                )
