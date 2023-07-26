from django.urls import path

from .views import (
    movie_list,
    movie_detail
)

urlpatterns = [
    path("movies/", movie_list, name="movie-list"),
    path("movies/<int:pk>/", movie_detail, name="movie-detail"),
    path("movies/", movie_list, name="movie-create"),
    path("movies/<int:pk>/", movie_detail, name="movie-update"),
    path("movies/<int:pk>/", movie_detail, name="movie-delete"),
]

app_name = "cinema"
