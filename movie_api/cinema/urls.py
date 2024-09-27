from django.urls import path

from cinema.views import (
    movie_api_get_post_list,
    movie_api_get_put_delete_by_id
)

urlpatterns = [
    path("movies/", movie_api_get_post_list, name="movies-list"),
    path(
        "movies/<int:pk>/",
        movie_api_get_put_delete_by_id,
        name="get-movie-by-id"
    ),
]

app_name = "cinema"
