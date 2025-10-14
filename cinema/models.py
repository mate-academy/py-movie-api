from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True)
    duration = models.IntegerField()


    class Meta:
        verbose_name_plural = "movies"

    def __str__(self):
        return (f"Movies: {self.title} - "
                f"duration: {self.duration} "
                f"(id = {self.id})")

