from django.urls import path

from cinema.views import movies, change_movie

app_name = "cinema"

urlpatterns = [
    path("movies/", movies, name="movie-list"),
    path("movies/<pk>/", change_movie, name="change-movie"),
]
