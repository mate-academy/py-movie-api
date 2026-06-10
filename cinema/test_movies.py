from django.test import TestCase, Client
from django.urls import reverse

from .models import Movie


class MovieAPITest(TestCase):
    def setUp(self):
        self.client = Client()

        self.movie = Movie.objects.create(
            title="Inception",
            description="Sci-fi movie",
            duration=148
        )

        self.movie_list_url = "/movies/"
        self.movie_detail_url = f"/movies/{self.movie.id}/"

    def test_get_movie_list(self):
        response = self.client.get(self.movie_list_url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)
        self.assertEqual(response.json()[0]["title"], "Inception")

    def test_create_movie(self):
        payload = {
            "title": "Interstellar",
            "description": "Space travel",
            "duration": 169
        }

        response = self.client.post(
            self.movie_list_url,
            data=payload,
            content_type="application/json"
        )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(Movie.objects.count(), 2)
        self.assertEqual(response.json()["title"], "Interstellar")

    def test_get_movie_detail(self):
        response = self.client.get(self.movie_detail_url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["title"], "Inception")

    def test_update_movie(self):
        payload = {
            "title": "Inception Updated",
            "description": "Updated desc",
            "duration": 150
        }

        response = self.client.put(
            self.movie_detail_url,
            data=payload,
            content_type="application/json"
        )

        self.assertEqual(response.status_code, 200)

        self.movie.refresh_from_db()
        self.assertEqual(self.movie.title, "Inception Updated")

    def test_delete_movie(self):
        response = self.client.delete(self.movie_detail_url)

        self.assertEqual(response.status_code, 204)
        self.assertEqual(Movie.objects.count(), 0)