from django.urls import path

from cinema.views import movie_list, movie_detail


urlpatterns = [
    path("movies/", movie_list, name="movies-list"),
    path("movies/<pk>/", movie_detail, name="movie-manager"),
]

app_name = "cinema"
