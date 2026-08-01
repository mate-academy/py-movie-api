from django.urls import path

from cinema.views import movie_list, movie_details

urlpatterns = [
    path("cinema/movies/", movie_list, name="cinema-movies"),
    path("cinema/movies/<int:pk>/", movie_details,
         name="cinema-movie-details"),
]

app_name = "cinema"
