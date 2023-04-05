from django.urls import path

from .views import retrieve_cinema, get_movies

urlpatterns = [
    path("movies/", get_movies, name="movies-list"),
    path("movies/<int:pk>/", retrieve_cinema, name="movie-detail"),
]
app_name = "cinema"
