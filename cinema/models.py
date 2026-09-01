from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=256, null=False, blank=False)
    description = models.CharField(max_length=1000, blank=True)
    duration = models.IntegerField()

    class Meta:
        verbose_name_plural = "movies"

    def __str__(self):
        return f"Movie title: {self.title}; duration: {self.duration}."
