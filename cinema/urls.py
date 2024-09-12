from django.urls import path

from .views import (
    movie_list,
    movie_datail
)

urlpatterns = [
    path("movies/", movie_list, name="movie-list"),
    path("movies/<int:pk>/", movie_datail, name="movie-detail")
]

app_name = "cinema"
