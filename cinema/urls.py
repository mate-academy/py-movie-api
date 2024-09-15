from django.urls import path

from cinema.views import movie_list, movie_edit, movie_delete

urlpatterns = [
    path("movies/", movie_list, name="cinema-list"),
    path("movies/<int:pk>/", movie_edit, name="movie-edit"),
    path("movies/<int:pk>/delete/", movie_delete, name="movie-delete"),
]

app_name = "cinema"
