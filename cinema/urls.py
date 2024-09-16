from django.contrib import admin
from django.urls import path, include

from cinema.views import movie_list, movie_detail

urlpatterns = [
    path("api/cinema/movies/", movie_list, name="movie-list"),
    path("api/cinema/movies/<int:pk>/", movie_detail, name="movie-detail"),
]

app_name = "cinema"
