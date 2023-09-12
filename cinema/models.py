from django.db import models


# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=60)
    description = models.CharField(max_length=255)
    duration = models.IntegerField()

    def __str__(self):
        return self.title
