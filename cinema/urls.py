from cinema.views import movie_list, movie_detail
from django.urls import path

app_name = "cinema"

urlpatterns = [
    path("movies/", movie_list, name="movie-list"),
    path("movies/<int:pk>/", movie_detail, name="movie-detail"),
]
