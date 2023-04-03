from django.urls import path

from cinema.views import movie_retrieve_create, movie_get_update_delete

app_name = "cinema"

urlpatterns = [
    path(
        "movies/",
        movie_retrieve_create,
        name="movie_retrieve_create"
    ),
    path(
        "movies/<int:pk>/",
        movie_get_update_delete,
        name="movie_get_update_delete"
    ),
]
