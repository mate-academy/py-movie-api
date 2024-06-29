from django.db import models

class Movies(models.Model):
    title = models.CharField(max_length=255, null=True)
    description = models.TextField(max_length=255, null=True)
    duration = models.IntegerField()

    class Meta:
        verbose_name_plural = "movies"

    def __str__(self):
        return f"Movies: {self.title} (id = {self.id})"
