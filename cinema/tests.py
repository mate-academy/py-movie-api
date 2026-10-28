import json

from django.urls import reverse
from rest_framework import status
from django.test import TestCase
from cinema.models import Movie
from cinema.serializers import MovieSerializer


class MovieModelTest(TestCase):
	def test_movie_create(self):
		movie = Movie.objects.create(
			title="Gladiator",
			description="A former Roman general sets out to exact vengeance...",
			duration=155
		)
		self.assertEqual(Movie.objects.count(), 1)
		self.assertEqual(movie.title, "Gladiator")
		self.assertEqual(movie.description, "A former Roman general sets out to exact vengeance...")
		self.assertEqual(movie.duration, 155)

	def test_movie_str(self):
		movie = Movie.objects.create(
			title="Avatar",
			description="A paraplegic marine dispatched to the moon Pandora...",
			duration=162
		)
		self.assertEqual(str(movie), "'Avatar'. Duration: 162 minutes.")

class MovieViewTest(TestCase):
	def setUp(self):
		self.movie = Movie.objects.create(
			title="Inception",
			description="A thief who steals corporate secrets...",
			duration=148
		)
		self.list_url = reverse("cinema:movie_list")
		self.detail_url = reverse("cinema:movie_detail", kwargs={"pk": self.movie.id})

	def test_get_movie_list(self):
		response = self.client.get(self.list_url)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		response_data = response.json()
		self.assertEqual(len(response_data), 1)
		self.assertEqual(response_data[0]["title"], self.movie.title)

	def test_create_movie(self):
		data = {
			"title": "Interstellar",
			"description": "A team of explorers travel through a wormhole...",
			"duration": 169
		}
		response = self.client.post(
			self.list_url,
			data=data,
			content_type="application/json"
		)
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		self.assertEqual(Movie.objects.count(), 2)
		response_data = response.json()
		self.assertEqual(Movie.objects.get(id=response_data["id"]).title, "Interstellar")

	def test_update_movie_put(self):
		data = {
			"title": "Inception Remastered",
			"description": "Updated description",
			"duration": 150
		}
		response = self.client.put(
			self.detail_url,
			data=json.dumps(data),
			content_type="application/json"
		)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.movie.refresh_from_db()
		self.assertEqual(self.movie.title, "Inception Remastered")
		self.assertEqual(self.movie.duration, 150)

	def test_delete_movie(self):
		response = self.client.delete(self.detail_url)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(Movie.objects.count(), 0)


class MovieSerializerTest(TestCase):
	def test_movie_serialization(self):
		movie = Movie.objects.create(
			title="Interstellar",
			description="A team of explorers travel through a wormhole...",
			duration=169
		)
		serializer = MovieSerializer(movie)
		expected_data = {
			"id": movie.id,
			"title": "Interstellar",
			"description": "A team of explorers travel through a wormhole...",
			"duration": 169
		}
		self.assertEqual(serializer.data, expected_data)

	def test_movie_deserialization_valid(self):
		data = {
			"title": "Matrix",
			"description": "A computer hacker learns from mysterious rebels...",
			"duration": 136
		}
		serializer = MovieSerializer(data=data)
		self.assertTrue(serializer.is_valid())
		self.assertEqual(serializer.validated_data["title"], "Matrix")

	def test_movie_deserialization_missing_title(self):
		data = {
			"description": "Some description without title",
			"duration": 120
		}
		serializer = MovieSerializer(data=data)
		self.assertFalse(serializer.is_valid())