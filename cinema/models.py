from django.db import models
from django.db.models import CharField, TextField, IntegerField


class Movie(models.Model):
    title = CharField(max_length=255)
    description = TextField()
    duration = IntegerField()

    def __str__(self):
        return self.title
