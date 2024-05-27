from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(blank=True, max_length=500)
    duration = models.IntegerField()

    def __str__(self):
        return f"Movie: {self.title}"

    class Meta:
        app_label = "cinema"
