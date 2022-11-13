from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True)
    duration = models.IntegerField()

    def str(self):
        return self.title
