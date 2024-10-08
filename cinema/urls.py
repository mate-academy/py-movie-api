from django.urls import path

from cinema.views import get_or_create_movie, get_update_or_delete_movie

app_name = "cinema"

urlpatterns = [
    path("movies/", get_or_create_movie, name="movies"),
    path("movies/<int:pk>", get_update_or_delete_movie, name="movie"),
]
