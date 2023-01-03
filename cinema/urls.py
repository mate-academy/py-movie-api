from django.urls import path

from cinema.views import *

urlpatterns = [
    path("movies/", movies_list, name="movies-list"),
    path("movies/<pk>/", movie_instance, name="movie-instance"),
]

app_name = "cinema"
