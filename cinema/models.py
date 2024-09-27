from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.title} ({self.duration} minutes)"

    class Meta:
        constraints = [
            models.CheckConstraint(condition=models.Q(duration__gt=0), name="duration_gt_0" )
        ]
