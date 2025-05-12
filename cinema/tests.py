from rest_framework.test import APITestCase
from rest_framework import status
from .models import Movie


class MovieAPITestCase(APITestCase):

    def setUp(self):
        self.movie_data = {
            "title": "Test Movie",
            "description": "This is a test movie.",
            "duration": 120
        }
        self.movie = Movie.objects.create(**self.movie_data)
        self.url = "/api/cinema/movies/"

    def test_create_movie(self):
        response = self.client.post(self.url, self.movie_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], self.movie_data["title"])

    def test_get_movies(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], self.movie_data["title"])

    def test_get_movie_detail(self):
        response = self.client.get(f"{self.url}{self.movie.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.movie_data["title"])

    def test_update_movie(self):
        updated_data = {
            "title": "Updated Movie",
            "description": "Updated description.",
            "duration": 150
        }
        response = self.client.put(f"{self.url}{self.movie.id}/", updated_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], updated_data["title"])

    def test_delete_movie(self):
        response = self.client.delete(f"{self.url}{self.movie.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Movie.objects.count(), 0)
