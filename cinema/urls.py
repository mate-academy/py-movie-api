from django.urls import path

from cinema.views import movies, change_movie

app_name = "cinema"

urlpatterns = [
    path("cinema/movies/", movies, name="movie-list"),
    path("cinema/movies/<pk>/", change_movie, name="change-movie"),
]
