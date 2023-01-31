from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255, verbose_name="Film title")
    description = models.TextField(verbose_name="Film description")
    duration = models.IntegerField(max_length=50, verbose_name="Film duration (min)")
