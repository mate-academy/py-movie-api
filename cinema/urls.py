
from django.urls import path

from cinema.views import movie_list, movie_detail

urlpatterns = [
    path("movie/", movie_list, name="movie-list"),
    path("movie/<pk>/", movie_detail, name="movie-detailed"),
]

app_name = "movie_app"
