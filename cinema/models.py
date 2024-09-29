from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    duration = models.IntegerField(null=False)

    def __str__(self):
        return f"{self.title} {self.duration}"
