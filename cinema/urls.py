from django.urls import path, include

from cinema.views import get_list_movies, get_detail_movie

urlpatterns = [
    path("movies/", get_list_movies, name="movies"),
    path("movies/<int:pk>/", get_detail_movie, name="movie_detail"),
]

app_name = "cinema"
