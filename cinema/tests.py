from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from cinema.models import Movie


class MovieApiTests(APITestCase):
    def setUp(self):
        self.payload = {
            "title": "Inception",
            "description": "A team enters shared dreams.",
            "duration": 148,
        }
        self.movie = Movie.objects.create(**self.payload)
        self.list_url = reverse("cinema:movie-list")
        self.detail_url = reverse("cinema:movie-detail", args=[self.movie.pk])

    def test_list_movies(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data, [{"id": self.movie.pk, **self.payload}]
        )

    def test_empty_list(self):
        Movie.objects.all().delete()
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [])

    def test_retrieve_movie(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {"id": self.movie.pk, **self.payload})

    def test_create_movie(self):
        response = self.client.post(self.list_url, self.payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        movie = Movie.objects.get(pk=response.data["id"])
        for field, value in self.payload.items():
            self.assertEqual(getattr(movie, field), value)
        self.assertEqual(Movie.objects.count(), 2)

    def test_client_cannot_choose_primary_key(self):
        response = self.client.post(
            self.list_url, {"id": 9999, **self.payload}, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertNotEqual(response.data["id"], 9999)

    def test_update_movie(self):
        payload = {
            "title": "Looper",
            "description": "A time travel thriller.",
            "duration": 119,
        }
        response = self.client.put(self.detail_url, payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.movie.refresh_from_db()
        for field, value in payload.items():
            self.assertEqual(getattr(self.movie, field), value)
        self.assertEqual(Movie.objects.count(), 1)

    def test_delete_movie(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(response.content, b"")
        self.assertFalse(Movie.objects.filter(pk=self.movie.pk).exists())

    def test_missing_movie_returns_404(self):
        url = reverse("cinema:movie-detail", args=[9999])
        for method in ("get", "put", "delete"):
            with self.subTest(method=method):
                response = getattr(self.client, method)(url)
                self.assertEqual(
                    response.status_code, status.HTTP_404_NOT_FOUND
                )

    def test_required_fields(self):
        for field in self.payload:
            with self.subTest(field=field):
                payload = self.payload.copy()
                payload.pop(field)
                response = self.client.post(
                    self.list_url, payload, format="json"
                )
                self.assertEqual(
                    response.status_code, status.HTTP_400_BAD_REQUEST
                )
                self.assertIn(field, response.data)
        self.assertEqual(Movie.objects.count(), 1)

    def test_invalid_field_values(self):
        invalid_values = {
            "title": ["", "   ", "x" * 256, None],
            "description": ["", None],
            "duration": [0, -1, 1.5, "invalid", None],
        }
        for field, values in invalid_values.items():
            for value in values:
                with self.subTest(field=field, value=value):
                    response = self.client.post(
                        self.list_url,
                        {**self.payload, field: value},
                        format="json",
                    )
                    self.assertEqual(
                        response.status_code, status.HTTP_400_BAD_REQUEST
                    )
                    self.assertIn(field, response.data)
        self.assertEqual(Movie.objects.count(), 1)

    def test_put_requires_complete_payload_and_preserves_movie_on_error(self):
        response = self.client.put(
            self.detail_url, {"title": "Changed"}, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.movie.refresh_from_db()
        self.assertEqual(self.movie.title, self.payload["title"])

    def test_unsupported_methods(self):
        for method, url in (
            ("delete", self.list_url),
            ("put", self.list_url),
            ("post", self.detail_url),
            ("patch", self.detail_url),
        ):
            with self.subTest(method=method, url=url):
                response = getattr(self.client, method)(url)
                self.assertEqual(
                    response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED
                )

    def test_malformed_json_returns_400(self):
        response = self.client.post(
            self.list_url, "{invalid", content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_prepared_fixture(self):
        from django.core.management import call_command

        call_command("loaddata", "cinema_service_db_data.json", verbosity=0)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)
        self.assertEqual(response.data[0]["title"], "The Departed")

