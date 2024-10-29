from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255, null=False)
    description = models.TextField(max_length=500, null=True, blank=True)
    duration = models.IntegerField()

    class Meta:
        verbose_name_plural = "movies"

    def __str__(self):
        return (f"title: {self.title}, "
                f"description: {self.description}, "
                f"duration: {self.duration}, "
                )
