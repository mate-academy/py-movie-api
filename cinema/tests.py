from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from cinema.models import Movie


class MovieAPITestCase(APITestCase):
    def setUp(self):
        self.movie = Movie.objects.create(
            title="Test Movie",
            description="A test movie.",
            duration=120
        )
        self.list_url = reverse("cinema:movie-list")
        self.detail_url = reverse("cinema:movie-detail", kwargs={"pk": self.movie.pk})

    def test_list_movies(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("title", response.data[0])
        self.assertEqual(response.data[0]["title"], self.movie.title)

    def test_retrieve_single_movie(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.movie.title)

    def test_create_movie(self):
        data = {
            "title": "Inception",
            "description": "Dreams within dreams.",
            "duration": 148
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Movie.objects.count(), 2)
        self.assertEqual(Movie.objects.last().title, "Inception")

    def test_update_movie(self):
        updated_data = {
            "title": "The Matrix",
            "description": "Sci-fi classic.",
            "duration": 136
        }
        response = self.client.put(self.detail_url, updated_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.movie.refresh_from_db()
        self.assertEqual(self.movie.title, "The Matrix")
        self.assertEqual(self.movie.duration, 136)

    def test_delete_movie(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Movie.objects.filter(pk=self.movie.pk).exists())
