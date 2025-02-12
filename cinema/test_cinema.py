from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from cinema.models import Movie


class MovieAPITestCase(APITestCase):
    def setUp(self):
        self.movie1 = Movie.objects.create(
            title="Movie 1", description="Some description", duration=100
        )
        self.movie2 = Movie.objects.create(
            title="Movie 2", description="Another description", duration=120
        )

        self.list_url = reverse("cinema:movies-list")

        self.detail_url = lambda pk: reverse(
            "cinema:movie-details", kwargs={"pk": pk}
        )

    def test_list_movies_returns_all_movies(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # movie1 and movie2
        self.assertEqual(response.data[0]["title"], self.movie1.title)

    def test_retrieve_movie_returns_correct_movie(self):
        response = self.client.get(self.detail_url(self.movie1.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Movie 1")
        self.assertEqual(response.data["duration"], 100)

    def test_create_movie_creates_new_movie(self):
        data = {
            "title": "New Movie",
            "description": "Brand new description",
            "duration": 95,
        }
        response = self.client.post(self.list_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(
            Movie.objects.count(), 3
        )
        self.assertEqual(response.data["title"], "New Movie")

    def test_update_movie_updates_existing_movie(self):
        update_data = {
            "title": "Updated Title",
            "description": "Updated Description",
            "duration": 200,
        }
        response = self.client.put(
            self.detail_url(self.movie1.id), update_data, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.movie1.refresh_from_db()
        self.assertEqual(self.movie1.title, "Updated Title")
        self.assertEqual(self.movie1.description, "Updated Description")
        self.assertEqual(self.movie1.duration, 200)

    def test_delete_movie_removes_movie(self):
        response = self.client.delete(self.detail_url(self.movie1.id))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        self.assertFalse(Movie.objects.filter(id=self.movie1.id).exists())
