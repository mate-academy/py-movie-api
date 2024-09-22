from django.contrib import admin
from django.urls import path

from cinema.views import movies_list, movie_detail

urlpatterns = [
    path("movies/", movies_list, name="movies_list"),
    path("movies/<int:pk>/", movie_detail, name="movie_detail"),
]

app_name = "cinema"
