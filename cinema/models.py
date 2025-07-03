from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=3000)
    duration = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Movies'

    def __str__(self):
        return f"id: {self.id}, {self.title}, duration: {self.duration}"
