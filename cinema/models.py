from django.db.models import (
    Model,
    CharField,
    TextField,
    IntegerField,
)


class Movie(Model):
    title = CharField(max_length=255)
    description = TextField()
    duration = IntegerField()

