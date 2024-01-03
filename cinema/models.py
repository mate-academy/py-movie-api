from django.db import models


# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=63)
    description = models.CharField(max_length=255, null=True)
    duration = models.IntegerField()

    class Meta:
        verbose_name_plural = 'movies'

    def __str__(self):
        return str(self.title)
