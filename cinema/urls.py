from django.urls import path
from .views import (
    movie_list,
    movie_detail,
)

urlpatterns = [
    path("movies/", movie_list, name="movie-list"),
    path("movies/<pk>/", movie_detail, name="movie-detail"),
]

app_name = "cinema"
