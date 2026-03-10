from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from cinema.models import Movie


class MovieViewsTestCase(APITestCase):
    fixtures = ['cinema_service_db_data.json']

    def test_movie_list(self):
        response = self.client.get("/api/cinema/movies/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 4)



    def test_create_movie(self):

        data = {
            "title": "Tenet",
            "description": "A secret agent is recruited by a mysterious organization called Tenet to prevent World War III",
            "duration": 120
        }

        response = self.client.post("/api/cinema/movies/", data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json()['title'], "Tenet")
        self.assertEqual(Movie.objects.count(), 5)



class MovieDetailsTestCase(APITestCase):
    fixtures = ['cinema_service_db_data.json']


    def test_movie_detail(self):
        response = self.client.get("/api/cinema/movies/1/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['title'], "The Departed")

    def test_update_movie(self):
        data = {
            "title": "Inception",
            "description": "A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O.",
            "duration": 123
        }
        response = self.client.put("/api/cinema/movies/1/", data, format='json' )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['duration'], 123)

    def test_delete_movie(self):
        response = self.client.delete("/api/cinema/movies/4/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(Movie.objects.filter(id=4).exists())
        self.assertEqual(Movie.objects.count(), 3)


    def test_delete_movie_false(self):
        response = self.client.delete("/api/cinema/movies/8/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)








