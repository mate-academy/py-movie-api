from django.urls import path
from cinema.views import movie_list, movie_detail

app_name = "movie"

urlpatterns = [
    path("movies/", movie_list, name="movie-list"),
    path("movies/<str:pk>/", movie_detail, name="movie-detail"),
]
