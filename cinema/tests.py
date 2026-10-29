import json

from django.test import TestCase
from django.urls import reverse

from .models import Movie


class MovieTests(TestCase):

    def setUp(self):
        self.movie = Movie.objects.create(
            title="Inception",
            description="A thief who steals corporate secrets through the use of dream-sharing technology...",
            duration=148
        )

    def test_create_movie(self):
        data = {
            "title": "Inception",
            "description": "A thief who steals corporate secrets through the use of dream-sharing technology...",
            "duration": 148
        }

        response = self.client.post(
            reverse("movie-list"),
            data=json.dumps(data),
            content_type="application/json"
        )

        self.assertEqual(response.status_code, 200)
        self.assertTrue(
            Movie.objects.filter(title="Inception").exists()
        )

    def test_movie_detail(self):
        response = self.client.get(
            reverse("movie-detail", kwargs={"pk": self.movie.pk})
        )

        self.assertEqual(response.status_code, 200)

        response_data = response.json()
        self.assertEqual(response_data["title"], "Inception")
        self.assertEqual(response_data["duration"], 148)

    def test_delete_movie(self):
        response = self.client.delete(
            reverse("movie-detail", kwargs={"pk": self.movie.pk})
        )

        self.assertEqual(response.status_code, 200)
        self.assertFalse(
            Movie.objects.filter(pk=self.movie.pk).exists()
        )
