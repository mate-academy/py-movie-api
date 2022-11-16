from django.urls import path

from cinema.views import movie_list, movie_info

urlpatterns = [
    path("movies/", movie_list, name="movie-list"),
    path("movies/<int:pk>/", movie_info, name="movie-info"),
]

app_name = "cinema"
