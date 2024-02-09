from django.urls import path

from cinema.views import movie_list

urlpatterns = [
    path("movies/", movie_list, name="movie-list"),
    path("movies/<int:pk>/", movie_list, name="get-movie"),
]

app_name = "cinema"
