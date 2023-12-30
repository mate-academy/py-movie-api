from django.urls import path

from cinema.views import movie_list, movie_current

urlpatterns = [
    path("movies/", movie_list, name="movie-list"),
    path("movies/<pk>/", movie_current, name="movie"),
]

app_name = "cinema"
