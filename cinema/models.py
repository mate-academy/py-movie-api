from django.db import models


# Create your models here.
class Movie(models.Model):
    title = models.CharField(null=False, max_length=155)
    description = models.CharField(max_length=1000)
    duration = models.IntegerField()
