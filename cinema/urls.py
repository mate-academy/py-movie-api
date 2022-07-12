from django.urls import path

from cinema.views import movie_list, get_movie

urlpatterns = [
    path("movies/", movie_list, name="movie-list"),
    path("movies/<int:pk>/", get_movie, name="assign-car"),
]

app_name = "cinema"
