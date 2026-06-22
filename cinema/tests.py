from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

from cinema.models import Movie
from cinema.serializers import MovieSerializer


class MovieApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.movie1 = Movie.objects.create(
            title="Titanic",
            description="Titanic description",
            duration=200,
        )
        self.movie2 = Movie.objects.create(
            title="Batman",
            description="Batman description",
            duration=190,
        )


    def test_get_movies(self):
        response = self.client.get("/api/cinema/movies/")
        serializer = MovieSerializer(Movie.objects.all(), many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), serializer.data)


    def test_get_movie(self):
        response = self.client.get(f"/api/cinema/movies/{self.movie2.id}/")
        serializer = MovieSerializer(self.movie2)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), serializer.data)


    def test_get_invalid_movie(self):
        response = self.client.get("/api/cinema/movies/9999/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


    def test_post_movie(self):
        data = {
            "title": "Superman",
            "description": "Superman description",
            "duration": 170,
        }
        response = self.client.post(
            "/api/cinema/movies/",
            data,
            content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Movie.objects.count(), 3)
        self.assertTrue(Movie.objects.filter(title="Superman").exists())

    def test_post_invalid_movie(self):
        data = {
            "title": "Superman",
            "description": "Superman description",
            "duration": "two hundred",
        }

        response = self.client.post(
            "/api/cinema/movies/",
            data,
            content_type="application/json"
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertFalse(Movie.objects.filter(title="Superman").exists())


    def test_put_movie(self):
        data = {
            "title": "Watchman",
            "description": "Watchman description",
            "duration": 190,
        }
        response = self.client.put(
            f"/api/cinema/movies/{self.movie1.id}/",
            data,
            content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.movie1.refresh_from_db()
        self.assertEqual(self.movie1.title, "Watchman")
        self.assertEqual(self.movie1.duration, 190)


    def test_put_invalid_movie(self):
        data = {
            "title": "Watchmen",
            "description": "Watchmen description",
            "duration": "fifty",
        }
        response = self.client.put(
            f"/api/cinema/movies/{self.movie1.id}/",
            data,
            content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.movie1.refresh_from_db()
        self.assertEqual(self.movie1.duration, 200)


    def test_delete_movie(self):
        response = self.client.delete(f"/api/cinema/movies/{self.movie1.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Movie.objects.filter(id=self.movie1.id).exists())


    def test_delete_invalid_movie(self):
        response = self.client.delete("/api/cinema/movies/9999/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)