from django.urls import path

from cinema.views import movie_list_create, movie_retrieve_patch_delete

app_name = "cinema"

urlpatterns = [
    path("movies/", movie_list_create, name="movie-list"),
    path(
        "movies/<int:pk>/",
        movie_retrieve_patch_delete,
        name="movie-detail"
    ),
]
