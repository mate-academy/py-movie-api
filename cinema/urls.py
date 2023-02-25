from cinema.views import movie_list, movie_object
from django.urls import path

urlpatterns = [
    path(
        "movies/",
        movie_list,
        name="movie-list"
    ),
    path(
        "movies/<int:pk>/",
        movie_object,
        name="movie-object"
    ),
]


app_name = "cinema"
