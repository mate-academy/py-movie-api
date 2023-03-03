from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=False, blank=False)
    duration = models.IntegerField(null=False, blank=False)

    class Meta:
        verbose_name = "movies"

    def __str__(self) -> str:
        return str(self.title)
