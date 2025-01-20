from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    description = models.TextField()
    duration = models.IntegerField()

    class Meta:
        verbose_name_plural = "Movies"

    def __str__(self) -> str:
        return f"Movie: {self.title} id: {self.id}"
