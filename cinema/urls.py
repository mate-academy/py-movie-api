from django.urls import path

from cinema.views import movie_list, get_movie

urlpatterns = [
    path("movies/", movie_list, name="movie_list"),
    path("movies/<int:pk>/", get_movie, name="movie"),
]

app_name = "cinema"
