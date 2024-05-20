from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=254)
    description = models.CharField(max_length=65)
    duration = models.IntegerField()

    class Meta:
        verbose_name_plural = "Movies"

    def __str__(self):
        return f"Movie title: {self.title}, description: {self.description}, duration: {self.duration}"
