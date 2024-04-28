from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(null=True)
    duration = models.IntegerField("Duration(min)")
