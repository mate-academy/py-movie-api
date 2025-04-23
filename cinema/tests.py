from rest_framework import status
from rest_framework.test import APITestCase
from cinema.models import Movie
from django.urls import reverse


class MovieAPITests(APITestCase):

    def setUp(self):
        self.movie = Movie.objects.create(
            title="Inception", description="Dream within a dream.", duration=148
        )
        self.movie_url = reverse("cinema:movie_detail", args=[self.movie.id])
        self.list_url = reverse("cinema:movie_list")

    def test_create_movie(self):
        data = {
            "title": "Interstellar",
            "description": "Space time travel.",
            "duration": 169,
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Movie.objects.count(), 2)

    def test_get_movies_list(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)
        self.assertGreaterEqual(len(response.data), 1)

    def test_get_single_movie(self):
        response = self.client.get(self.movie_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.movie.title)

    def test_update_movie(self):
        updated_data = {
            "title": "Inception Updated",
            "description": "Updated description.",
            "duration": 150,
        }
        response = self.client.put(self.movie_url, updated_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.movie.refresh_from_db()
        self.assertEqual(self.movie.title, "Inception Updated")

    def test_delete_movie(self):
        response = self.client.delete(self.movie_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Movie.objects.filter(id=self.movie.id).exists())
