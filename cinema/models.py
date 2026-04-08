from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    duration = models.IntegerField()

    class Meta:
        db_table = "movie"

    def __str__(self):
        return f"title: {self.title} duration: {self.duration} description: {self.description}"
