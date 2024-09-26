from django.urls import path

from cinema.views import get_or_create_movie, get_update_delete_movie

app_name = "cinema"

urlpatterns = [
    path("", get_or_create_movie, name="movie-list"),
    path("movie/<int:pk>/", get_update_delete_movie, name="movie-detail"),
]