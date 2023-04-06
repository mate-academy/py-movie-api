from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=63)
    description = models.TextField()
    duration = models.IntegerField(null=True)

    def __str__(self):
        return self.title
