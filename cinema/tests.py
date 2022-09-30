from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse

from cinema.models import Movie

from rest_framework.test import APIClient


class TestCinemaApiCRUD(TestCase):
    @classmethod
    def setUpTestData(cls):
        Movie.objects.create(
            title="TestTitle",
            description="TestDescription",
            duration=120
        )

    def test_post_method(self):
        response = self.client.post(
            reverse("cinema:cinema-POST-GET-all"),
            data={
                "title": "NewTitle",
                "description": "NewDescription",
                "duration": 150
            },
            HTTP_ACCEPT="application/json"
        )
        movie = Movie.objects.get(pk=2)
        self.assertEqual(response.status_code, HTTPStatus.CREATED)
        self.assertEqual(response.json()["title"], movie.title)

    def test_get_method(self):
        response = self.client.get(reverse("cinema:cinema-GET-PUT-DELETE", kwargs={"pk": 1}))
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.json()["title"], "TestTitle")

    def test_put_method(self):
        client = APIClient()
        response = client.put(
            reverse("cinema:cinema-GET-PUT-DELETE", kwargs={"pk": 1}),
            {
                "title": "RenameTitle",
                "description": "TestDescription",
                "duration": 120
            }

        )
        self.assertEqual(response.status_code, HTTPStatus.ACCEPTED)
        self.assertEqual(response.json()["title"], "RenameTitle")

    def test_delete_method(self):
        response = self.client.delete(reverse("cinema:cinema-GET-PUT-DELETE", kwargs={"pk": 1}))
        self.assertEqual(response.status_code, HTTPStatus.NO_CONTENT)
