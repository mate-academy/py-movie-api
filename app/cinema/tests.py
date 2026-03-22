from tkinter.font import names

from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse

from .models import Movie
from .serializers import MovieSerializer
from .views import movie_list


class MovieViewsTest(APITestCase):
    def setUp(self):
        self.list_url = reverse("cinema:movie-list")
        self.detail_url = reverse("cinema:movie-detail", args=[1])

        self.movie = Movie.objects.create(
            title = "Terminator",
            description = "Terminator in the fire",
            duration = 130,
        )
        self.movie = Movie.objects.create(
            title="Immortals",
            description="Test description",
            duration=110,
        )
        self.movie = Movie.objects.create(
            title="Fast and furious",
            description="Street car racing",
            duration=125,
        )

    def test_list_get_method(self):
        response = self.client.get(self.list_url)

        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)

    def test_list_post_method(self):
        data = {"title": "Create", "description": "Testing", "duration": 120}
        response = self.client.post(self.list_url, data=data)

        self.assertEqual(response.status_code, 201)
        self.assertTrue(Movie.objects.filter(title="Create").exists())

    def test_detail_get_method(self):
        response = self.client.get(self.detail_url)

        movie = Movie.objects.get(pk=1)
        serializer = MovieSerializer(movie)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)

    def test_detail_put_method(self):
        data = {"title": "Update data", "description": "Put method", "duration": 120}
        response = self.client.put(self.detail_url, data=data)

        movie = Movie.objects.get(pk=1)
        serializer = MovieSerializer(movie)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data, serializer.data)

    def test_detail_delete_method(self):
        response = self.client.delete(self.detail_url)

        self.assertEqual(response.status_code, 204)
        self.assertFalse(Movie.objects.filter(title="Terminator").exists())
