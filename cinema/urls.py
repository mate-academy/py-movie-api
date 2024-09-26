from django.urls import path

from cinema.views import list_or_create_movie, get_update_delete_movie

app_name = "cinema"

urlpatterns = [
    path("movies/", list_or_create_movie, name="list-or-create-movie"),
    path(
        "movies/<int:pk>/",
        get_update_delete_movie,
        name="get-update-delete-movie"
    ),
]
