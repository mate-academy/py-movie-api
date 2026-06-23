from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    description = models.CharField(max_length=255)
    duration = models.FloatField()

    class Meta:
        verbose_name_plural = "movies"

    def __str__(self):
        return f"Movie {self.title}, duration {self.duration}"
