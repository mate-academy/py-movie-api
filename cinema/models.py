from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True)
    duration = models.IntegerField()

    def __str__(self) -> str:
        return self.title
