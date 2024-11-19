from django.db import models

# Create your models here.


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    duration = models.IntegerField()

    class Meta:
        verbose_name_plural = "Movies"

    def __str__(self):
        return f"Title:{self.title}, duration:{self.duration}"
