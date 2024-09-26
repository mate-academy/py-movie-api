from django.urls import path

from .views import movie_list_create, movie_detail_retrieve_update_delete

app_name = "cinema"

urlpatterns = [
    path("movies/", movie_list_create, name="movie-list"),
    path(
        "movies/<int:pk>/",
        movie_detail_retrieve_update_delete,
        name="movie-detail"
    ),
]
