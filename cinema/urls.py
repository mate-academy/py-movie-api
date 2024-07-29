from django.urls import path

from cinema.views import movie_list, movie_details


app_name = "cinema"

urlpatterns = [
    path("movies/", movie_list, name="movie-list"),
    path("movies/<int:pk>/", movie_details, name="movie-details"),
]
