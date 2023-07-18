from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    duration = models.IntegerField(help_text="A film duration in minutes")
