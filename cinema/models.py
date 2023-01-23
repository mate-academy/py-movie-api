from django.db import models


class Actor(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)


class Genre(models.Model):
    name = models.CharField(max_length=255, unique=True)


class CinemaHall(models.Model):
    name = models.CharField(max_length=255)
    rows = models.IntegerField()
    seats_in_row = models.IntegerField()


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    duration = models.IntegerField()
    actors = models.ManyToManyField(Actor, related_name="actors")
    genres = models.ManyToManyField(Genre, related_name="genres")

    class Meta:
        verbose_name_plural = "movies"

    def __str__(self):
        return str(self.title)
