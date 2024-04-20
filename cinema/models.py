from django.db import models

# Create your models here.
#


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=500)
    duration = models.IntegerField()

    class Meta:
        verbose_name = "movies"

    def __str__(self) -> str:
        return f"{self.title}: {self.description}"
