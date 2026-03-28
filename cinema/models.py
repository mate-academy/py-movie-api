from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    duration = models.IntegerField()

    class Meta:
        db_table = "movie"

    def __str__(self):
        return f"movie title: {self.title}, description: {self.description}, duration: {self.duration}"
