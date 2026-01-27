from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    duration = models.PositiveIntegerField()

    class Meta:
        verbose_name_plural = "movies"


    def __str__(self):
        return f"Movie: {self.title} (id = {self.id})"
