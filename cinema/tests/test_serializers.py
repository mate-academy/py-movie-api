from django.test import TestCase
from cinema.models import Movie
from cinema.serializers import MovieSerializer


class MovieSerializerTest(TestCase):

    def setUp(self):
        self.valid_data = {
            "title": "Inception",
            "description": "Mind-bending thriller",
            "duration": 148
        }

        self.invalid_data = {
            "title": "",
            "description": "No title here",
            "duration": None
        }

        self.empty_description = {
            "title": "Test_title",
            "description": "",
            "duration": 150
        }

        self.movie = Movie.objects.create(**self.valid_data)

    def test_valid_data_is_valid(self):
        serializer = MovieSerializer(data=self.valid_data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.errors, {})

    def test_invalid_data_is_not_valid(self):
        serializer = MovieSerializer(data=self.invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("title", serializer.errors)
        self.assertIn("duration", serializer.errors)

    def test_empty_description(self):
        serializer = MovieSerializer(data=self.empty_description)
        self.assertFalse(serializer.is_valid())
        self.assertIn("description", serializer.errors)

    def test_serializer_output_fields(self):
        serializer = MovieSerializer(self.movie)
        self.assertEqual(serializer.data["title"], "Inception")
        self.assertEqual(serializer.data["duration"], 148)

    def test_create_movie_from_serializer(self):
        serializer = MovieSerializer(data=self.valid_data)
        self.assertTrue(serializer.is_valid())
        movie = serializer.save()
        self.assertIsInstance(movie, Movie)
        self.assertEqual(movie.title, "Inception")
