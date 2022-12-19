from django.urls import path

from cinema.views import movie_list, movie_modification


urlpatterns = [
    path("movies/", movie_list, name="movie-list"),
    path("movies/<pk>/", movie_modification, name="movie-modification"),
]

app_name = "cinema"
