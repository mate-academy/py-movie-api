from django.urls import path
from cinema.views import movie_list

app_name = "cinema"

urlpatterns = [
    path("movies/", movie_list, name="movie-list"),
]

