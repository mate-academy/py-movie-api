from django.urls import path

from cinema.views import movie_list, movie

urlpatterns = [
    path("movies/", movie_list, name="movie-list"),
    path("movies/<pk>/", movie, name="movie"),
]

app_name = "cinema"
