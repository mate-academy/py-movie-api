from django.db import models
from django.db.models import CheckConstraint, Q


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=511)
    duration = models.IntegerField()
