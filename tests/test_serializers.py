from django.test import TestCase
from cinema.models import Movie
from cinema.serializers import MovieSerializer


class MovieSerializerTest(TestCase):
    def test_serialization(self):
        movie = Movie.objects.create(
            title="Interstellar",
            description="Space travel",
            duration=169
        )
        serializer = MovieSerializer(movie)
        expected_data = {
            "id": movie.id,
            "title": "Interstellar",
            "description": "Space travel",
            "duration": 169
        }
        self.assertEqual(serializer.data, expected_data)
