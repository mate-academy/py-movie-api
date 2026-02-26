from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from cinema.serializers import MovieSerializer
from cinema.models import Movie


class MovieApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        Movie.objects.create(title="Harry Potter 1",
                             description="some description1",
                             duration="129")
        Movie.objects.create(title="Harry Potter 2",
                             description="some description2",
                             duration="1")
        Movie.objects.create(title="Harry Potter 3",
                             description="some description3",
                             duration="122")
        Movie.objects.create(title="Harry Potter 4",
                             description="some description4",
                             duration="122")

    def test_get_movies(self):
        response = self.client.get("/api/v1/cinema/movies/")
        serializer = MovieSerializer(Movie.objects.all(), many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_get_movie(self):
        movie = Movie.objects.get(pk=1)
        response = self.client.get(f"/api/v1/cinema/movies/{movie.pk}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serializer = MovieSerializer(movie)
        self.assertEqual(response.data, serializer.data)

    def test_delete_movie(self):
        movie = Movie.objects.get(pk=1)
        response = self.client.delete(f"/api/v1/cinema/movies/{movie.pk}/")
        exists = Movie.objects.filter(pk=movie.pk).exists()
        self.assertFalse(exists)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_nonexistent_movie(self):
        response = self.client.delete("/api/v1/cinema/movies/99999/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_deleted_movie(self):
        movie = Movie.objects.create(title="temp",
                                     description="temp",
                                     duration=2)
        movie.delete()
        response = self.client.delete(f"/api/v1/cinema/movies/{movie.pk}/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_movie(self):
        data = {
            "title": "temp",
            "description": "temp",
            "duration": 120
        }
        response = self.client.post("/api/v1/cinema/movies/",
                                    data,
                                    format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        exists = Movie.objects.filter(title="temp",
                                      description="temp").exists()
        self.assertTrue(exists)

    def test_create_movie_with_bad_data(self):
        response = self.client.post(
            "/api/v1/cinema/movies/",
            {"title": "test", "description": "test", "duration": -22},
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        exists = Movie.objects.filter(title="test",
                                      description="test").exists()
        self.assertFalse(exists)

    def test_put_movie(self):
        movie = Movie.objects.all().first()
        new_data = {
            "title": "New Title",
            "description": "New description",
            "duration": 9999
        }
        response = self.client.put(f"/api/v1/cinema/movies/{movie.pk}/",
                                   new_data,
                                   format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        movie.refresh_from_db()
        self.assertEqual(movie.title, "New Title")
        self.assertEqual(movie.description, "New description")
        self.assertEqual(movie.duration, 9999)
