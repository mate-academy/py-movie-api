from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False)
    description = models.TextField(blank=True)
    duration = models.TimeField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "movies"

    def __str__(self):
        return f"{self.title} (duration : {self.duration} min)"
