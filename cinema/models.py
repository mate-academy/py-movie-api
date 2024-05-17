from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(null=True, blank=True, max_length=500)
    duration = models.IntegerField()

    class Meta:
        app_label = "cinema"
