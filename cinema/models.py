from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255, help_text="Movie title")
    description = models.TextField(help_text="Movie plot description")
    duration = models.PositiveSmallIntegerField(help_text="Movie duration in minutes")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = "Movie"
        verbose_name_plural = "Movies"
