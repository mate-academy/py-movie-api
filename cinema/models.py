from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    duration = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name = "movies"

    def __str__(self):
        return str(self.title)
