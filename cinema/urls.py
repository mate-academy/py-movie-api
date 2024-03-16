from django.urls import path
from cinema.views import movie_detail, movie_list

app_name = "cinema"

urlpatterns = [
    path("cinema/movies/", movie_list, name="movie-list"),
    path("cinema/movies/<int:pk>/", movie_detail, name="movie-detail"),
]
