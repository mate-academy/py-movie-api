from django.urls import path

from cinema.views import movie_list, movie_details

urlpatterns = [
    path("movies/", movie_list, name="movies-list"),
    path("movies/<int:pk>", movie_details, name="movie-details")
]

app_name = "cinema"
