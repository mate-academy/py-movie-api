from django.urls import path
from cinema.views import Movie_list, Movie_detail

app_name = "cinema"


urlpatterns = [
    path("movies/", Movie_list, name="movie_list"),
    path("movies/<int:pk>/", Movie_detail, name="movie_detail"),
]
