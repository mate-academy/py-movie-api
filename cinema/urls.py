from django.urls import path

from cinema.views import (
    movie_list_create,
    movie_detail_update_delete,
)


app_name = "cinema"

urlpatterns = [
    path("movies/", movie_list_create, name="movie-list-create"),
    path("movies/<int:pk>/", movie_detail_update_delete, name="movie-detail-update-delete"),
]
