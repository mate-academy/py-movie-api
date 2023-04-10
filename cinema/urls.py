from django.urls import path

from cinema.views import movies_list, movie_detail

urlpatterns = [
    path("movies/", movie_list, name="movie-list"),

    path("movies/<pk>/", movie_detail, name="movie-detailed"),
]

app_name = "cinema"
