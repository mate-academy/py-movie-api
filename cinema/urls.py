from django.urls import path
from cinema.views import movie_list, movie_detail

urlpatterns = [
    path("movies/<int:pk>/", movie_detail, name="movie-detail"),
    path("movies/", movie_list, name="movie-list")
]

app_name = "cinema"
