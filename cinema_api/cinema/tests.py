from django.test import TestCase

from rest_framework.test import APIClient

from .models import Movie


class MovieApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.movie = Movie.objects.create(
            title="Test Movie",
            description="Test description",
            duration=120,
        )

    def test_movie_list(self):
        response = self.client.get("/api/cinema/movies/")
        self.assertEqual(response.status_code, 200)

    def test_movie_post(self):
        response = self.client.post(
            "/api/cinema/movies/",
            data={
                "title": "Test Movie",
                "description": "Test description",
                "duration": 120,
            },
        )

        self.assertEqual(response.status_code, 201)

    def test_movie_put(self):
        movie = Movie.objects.create(
            title="Old title",
            description="Old description",
            duration=100,
        )

        response = self.client.put(
            f"/api/cinema/movies/{movie.id}/",
            data={
                "title": "New title",
                "description": "New description",
                "duration": 120,
            },
        )

        self.assertEqual(response.status_code, 200)

    def test_movie_detail(self):
        movie = Movie.objects.create(
            title="Test Movie",
            description="Test description",
            duration=120,

        )
        response = self.client.get(f"/api/cinema/movies/{movie.id}/")
        self.assertEqual(response.status_code, 200)

    def test_movie_delete(self):
        movie = Movie.objects.create(
            title="Old title",
            description="Old description",
            duration=100,
        )

        response = self.client.delete(
            f"/api/cinema/movies/{movie.id}/"
        )
        self.assertEqual(response.status_code, 204)
