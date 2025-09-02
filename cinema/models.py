from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    duration = models.TimeField()
