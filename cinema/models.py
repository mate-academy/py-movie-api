from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    duration = models.DecimalField(max_digits=5, decimal_places=2)
