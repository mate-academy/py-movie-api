from django.contrib import admin
from django.urls import path

from cinema.views import movies_list, movies_detail


urlpatterns = [
    path("movies/", movies_list, name="movie-list"),
    path("movie/<int:movie_id>/", movies_detail, name="movie-detail"),
]

app_name = "cinema"
