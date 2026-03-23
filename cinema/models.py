from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.PositiveIntegerField()

    class Meta:
        verbose_name_plural = "movies"
        ordering = ["title"]

    def __str__(self):
        return f"{self.title}, {self.duration} minute(s)"
