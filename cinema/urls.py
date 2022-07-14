from django.urls import path

from cinema.views import movie_detail, change_movie

urlpatterns = [
    path("movies/", movie_detail, name="movie-list"),
    path("movies/<int:pk>/", change_movie, name="change-movie"),
]

app_name = "cinema"

