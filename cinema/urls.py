from django.urls import path

from cinema.views import movie_list, get_or_change_movie

urlpatterns = [
    path("movies/", movie_list, name="movie_list"),
    path("movies/<int:pk>/", get_or_change_movie, name="get_or_change_movie")
]

app_name = "cinema"
