from django.urls import path

from cinema.views import movie_list, movie_with_id

urlpatterns = [
    path("movies/", movie_list, name="movie-list"),
    path("movies/<int:pk>/", movie_with_id, name="movie")
]

app_name = "movie"
