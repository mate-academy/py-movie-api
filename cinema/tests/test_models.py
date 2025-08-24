from django.test import TestCase
from django.core.exceptions import ValidationError
from cinema.models import Movie


class ModelTest(TestCase):
    def test_movie_str(self):
        movie = Movie.objects.create(
            title="Test_title",
            description="Test description.",
            duration=100
        )
        self.assertEqual(str(movie), movie.title)
    
    def test_movie_with_empty_description(self):
        movie = Movie(
            title="Test_title",
            description="",
            duration=100
        )
        with self.assertRaises(ValidationError):
            movie.full_clean()

