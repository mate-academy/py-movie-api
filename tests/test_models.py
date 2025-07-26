from django.test import TestCase
from cinema.models import Movie


class MovieModelTest(TestCase):
    def test_str_representation(self):
        movie = Movie.objects.create(
            title="Inception",
            description="Dreams inside dreams",
            duration=148
        )
        self.assertEqual(str(movie), "Inception")