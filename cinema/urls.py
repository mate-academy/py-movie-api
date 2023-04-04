from django.urls import path

from cinema.views import movies

urlpatterns = [
    path("cinema/movies/", movies, name="movie-list"),
]