
from django.urls import path

from cinema.views import movie_list_api, movie_api

urlpatterns = [
    path("movies/", movie_list_api, name="movie-list"),
    path("movies/<int:pk>/", movie_api, name="movie"),
]
