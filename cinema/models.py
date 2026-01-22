from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=500)  # Usando CharField como sugerido pelo checklist
    duration = models.PositiveIntegerField()       # Duração em minutos

    def __str__(self):
        return self.title
