from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from cinema.serializers import (
    MovieSerializer
)


class TestMovieSerializer(TestCase):
    def test_create_movie(self):
        data = {
            "title": "The Godfather",
            "description": "The aging patriarch of an organized crime dynasty "
            "transfers control of his clandestine empire to his reluctant "
            "son.",
            "duration": 175
        }
        serializer = MovieSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        movie = serializer.save()
        self.assertEqual(movie.title, "The Godfather")
        self.assertEqual(movie.description, "The aging patriarch of an "
                         "organized crime dynasty transfers control of his "
                         "clandestine empire to his reluctant son.")
        self.assertEqual(movie.duration, 175)
