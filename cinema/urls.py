from django.urls import path

from .view import cinema_list, cinema_detail

app_name = "cinema"

urlpatterns = [
    path("movies/", cinema_list, name="cinema_list"),
    path("movies/<int:pk>/", cinema_detail, name="movie-detailed"),
]
