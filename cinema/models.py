from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True, blank=True)
    duration = models.PositiveIntegerField(help_text="Duration in minutes")

    class Meta:
        verbose_name_plural = "movies"

    def __str__(self):
        return self.title