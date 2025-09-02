from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)
    duration = models.IntegerField()

    def __str__(self):
        return f"Title: {self.title}"
