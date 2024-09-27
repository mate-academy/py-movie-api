from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255, null=False)
    description = models.CharField(max_length=255, null=False)
    duration = models.IntegerField(null=False)

    def __str__(self):
        return (
            f"Title: {self.title}, "
            f"Duration: {self.duration}"
        )
