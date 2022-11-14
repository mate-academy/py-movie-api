from django.urls import path

from .views import movie_list_view, movie_detail_view

url_templates = [
    path("movies/", movie_list_view, name="movie-list"),
    path("movies/<int:pk>", movie_detail_view, name="movie-detail")
]

app_name = "cinema"
