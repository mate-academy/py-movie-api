from django.urls import path

from cinema.views import list_movies, current_movie

urlpatterns = [
    path("movies/", list_movies, name="movie-list"),
    path("movies/<int:pk>/", current_movie, name="movie"),
]

app_name = "cinema"
