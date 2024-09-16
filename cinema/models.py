from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=70)
    description = models.TextField(blank=True, null=True)
    duration = models.IntegerField()

    class Meta:
        verbose_name_plural = "movies"
        ordering = ["title"]

    def __str__(self):
        return f"Title: {self.title}(duration: {self.duration} min.)"
