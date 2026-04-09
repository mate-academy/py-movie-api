from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from cinema.models import Movie


class MovieModelTest(TestCase):

    def test_movie_str_method(self):
        movie = Movie.objects.create(
            title="Inception",
            description="One of the best movies ever made",
            duration=90,
        )
        self.assertEqual(str(movie), "Inception")


class MovieApiTest(APITestCase):

    def setUp(self):
        Movie.objects.create(title="Avatar", duration=165)
        Movie.objects.create(title="Inception", duration=90)
        self.url = reverse("cinema:movie-list")

    def test_get_movie_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]["title"], "Avatar")

    def test_create_movie_valid_data(self):
        data = {"title": "Avatar II", "description": "Second epizode", "duration": 165}
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Movie.objects.count(), 3)


class MovieApiDetailTest(APITestCase):

    def setUp(self):
        self.movie = Movie.objects.create(
            title="Titanic",
            description="One of the most popular movie ine the history",
            duration=120,
        )
        self.url = reverse("cinema:movie-detail", kwargs={"pk": self.movie.pk})

    def test_movie_detail(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Titanic")

    def test_movie_detail_update(self):
        update_data = {
            "title": "Avatar",
            "description": "The best movie",
            "duration": 120,
        }
        response = self.client.put(self.url, update_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.movie.refresh_from_db()
        self.assertEqual(self.movie.title, "Avatar")

    def test_movie_detail_delete(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Movie.objects.count(), 0)

    def test_movie_detail_not_found(self):
        invalid_url = reverse("cinema:movie-detail", kwargs={"pk": 999})
        response = self.client.get(invalid_url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
