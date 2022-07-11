from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=50, null=False)
    description = models.TextField(null=True)
    duration = models.IntegerField(null=True)

    class Meta:
        verbose_name = "movie"
        verbose_name_plural = "movies"

    def __str__(self):
        return str(self.title)
