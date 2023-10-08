from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Movie


class MovieTests(APITestCase):
    def setUp(self):
        self.movie_data = {
            "title": "Test Movie",
            "description": "This is a test movie",
            "duration": 120,
        }
        self.movie = Movie.objects.create(**self.movie_data)
        self.url = reverse("cinema:movie-list")

    def test_create_movie(self):
        response = self.client.post(self.url, self.movie_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Movie.objects.count(), 2)

    def test_list_movies(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_retrieve_movie(self):
        url = reverse("cinema:movie-detail", args=[self.movie.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.movie.title)

    def test_update_movie(self):
        url = reverse("cinema:movie-detail", args=[self.movie.id])
        updated_data = {
            "title": "Updated Movie",
            "description": "This is an updated movie",
            "duration": 150,
        }
        response = self.client.put(url, updated_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        self.movie.refresh_from_db()
        self.assertEqual(self.movie.title, updated_data["title"])
        self.assertEqual(self.movie.description, updated_data["description"])
        self.assertEqual(self.movie.duration, updated_data["duration"])

    def test_delete_movie(self):
        url = reverse("cinema:movie-detail", args=[self.movie.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Movie.objects.count(), 0)
