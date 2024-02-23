from django.urls import path

from cinema.views import movie_list, movie_by_id

urlpatterns = [
    path("movies/", movie_list, name="movie-list"),
    path("movies/<int:pk>", movie_by_id, name="movie-by-id"),
]

app_name = "cinema"
