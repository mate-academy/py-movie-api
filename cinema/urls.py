from django.urls import path
from cinema.views import (
    movies, movie
)

urlpatterns = [
    path("movies/", movies, name="movies"),
    path("movies/<int:pk>/", movie, name="movie")
]

app_name = "cinema"
