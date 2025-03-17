from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    duration = models.IntegerField()

    class Meta:
        db_table = "movie"
        verbose_name_plural = "movies"

    def __str__(self):
        return (
            f"Movie:"
            f" (id={self.id}),"
            f" Title: {self.title},"
            f" Description: {self.description},"
            f" Duration: {self.duration}"
        )
