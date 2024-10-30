from django.test import TestCase
from django.urls import reverse
from .models import Movie
from rest_framework import status
from rest_framework.test import APIClient

class MovieModelTest(TestCase):
    def test_movie_creation(self):
        movie = Movie.objects.create(
            title="Sample Movie", description="A sample description", duration=120
        )
        self.assertEqual(movie.title, "Sample Movie")
        self.assertEqual(movie.duration, 120)

class MovieViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.movie = Movie.objects.create(
            title="Sample Movie", description="A sample description", duration=120
        )

    def test_get_movie_list(self):
        response = self.client.get(reverse("cinema:movie-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_movie_detail(self):
        response = self.client.get(reverse("cinema:movie-detail", args=[self.movie.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Sample Movie")

    def test_create_movie(self):
        data = {"title": "New Movie", "description": "New description", "duration": 90}
        response = self.client.post(reverse("cinema:movie-list"), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
