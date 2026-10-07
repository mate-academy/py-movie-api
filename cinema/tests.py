from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Movie

class MovieModelTest(TestCase):
    def test_create_movie(self):
        movie = Movie.objects.create(
            title="Inception",
            description="A mind-bending thriller",
            duration=148
        )
        self.assertEqual(movie.title, "Inception")
        self.assertEqual(Movie.objects.count(), 1)

class MovieAPITest(APITestCase):
    def test_list_movies(self):
        Movie.objects.create(title="Test", description="Desc", duration=100)
        response = self.client.get('/api/cinema/movies/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
