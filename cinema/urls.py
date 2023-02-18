from django.urls import path

from cinema.views import movie_list, movie_object


urlpatterns = [
    path("movies/", movie_list, name="movie-list"),
    path("movies/<int:pk>/", movie_object, name="movie")
]

app_name = "cinema"
