from django.urls import path

from cinema.views import movie_list, movie_change

urlpatterns = [
    path("movies/", movie_list, name="movies-list"),
    path(
        "movies/<int:pk>/",
        movie_change,
        name="get-movie-by-id"
    ),
]

app_name = "cinema"
