from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Movie
from .serializers import MovieSerializer


MOVIE_LIST_URL = reverse('cinema:movie-list-create')


def detail_url(movie_id):
    return reverse('cinema:movie-detail', args=[movie_id])


class MovieModelTest(APITestCase):

    def test_movie_creation(self):

        movie = Movie.objects.create(
            title='Test Movie',
            description='This is a test description.',
            duration=120
        )
        self.assertEqual(movie.title, 'Test Movie')
        self.assertEqual(movie.duration, 120)
        self.assertTrue(isinstance(movie, Movie))

    def test_movie_str(self):
        movie = Movie.objects.create(
            title='Dune', description='Epic saga', duration=155)
        self.assertEqual(str(movie), 'Dune')


class MovieAPITest(APITestCase):

    def setUp(self):
        self.movie1 = Movie.objects.create(
            title='Movie 1',
            description='Description 1',
            duration=90
        )
        self.movie2 = Movie.objects.create(
            title='Movie 2',
            description='Description 2',
            duration=180
        )
        self.payload = {
            'title': 'New Movie Title',
            'description': 'New description content',
            'duration': 105
        }

    def test_retrieve_movies_list(self):
        response = self.client.get(MOVIE_LIST_URL)

        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(len(response.data), 2)

    def test_retrieve_movie_detail(self):
        url = detail_url(self.movie1.id)
        response = self.client.get(url)

        serializer = MovieSerializer(self.movie1)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_create_movie_successful(self):
        response = self.client.post(MOVIE_LIST_URL, self.payload)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Movie.objects.count(), 3)

        new_movie = Movie.objects.get(id=response.data['id'])
        self.assertEqual(new_movie.title, self.payload['title'])

    def test_create_movie_with_missing_field_fails(self):
        bad_payload = {'description': 'Description', 'duration': 100}
        response = self.client.post(MOVIE_LIST_URL, bad_payload)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('title', response.data)
        self.assertEqual(Movie.objects.count(), 2)

    def test_full_update_movie(self):
        url = detail_url(self.movie1.id)
        update_data = {
            'title': 'Updated Film',
            'description': 'New Description Content',
            'duration': 145
        }
        response = self.client.put(url, update_data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.movie1.refresh_from_db()
        self.assertEqual(self.movie1.title, update_data['title'])
        self.assertEqual(self.movie1.duration, 145)

    def test_delete_movie(self):
        url = detail_url(self.movie1.id)
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Movie.objects.count(), 1)

        with self.assertRaises(Movie.DoesNotExist):
            Movie.objects.get(id=self.movie1.id)
