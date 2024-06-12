from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.IntegerField()

    class Meta:
        verbose_name = "movies"

    def __str__(self):
        return (
            f"Movie: {self.title}, "
            f"Description: {self.description}, "
            f"Duration: {self.duration} "
        )
