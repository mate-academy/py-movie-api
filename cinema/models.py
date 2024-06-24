from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=250, null=True)
    duration = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Movies'

    def __str__(self):
        return f"title: {self.title}; duration: {self.duration}"
