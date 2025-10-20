from django.urls import path
from .views import movie_list, get_movie


urlpatterns = [
    path("movies/", movie_list, name="movie-list"),
    path("movies/<int:pk>/", get_movie, name="movie-detailed"),
]

app_name = "cinema"
