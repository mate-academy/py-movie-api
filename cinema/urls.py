from django.urls import path, include

from cinema.views import movie_list, movie_object

urlpatterns = [
    path("movies/", movie_list, name="movie-list"),
    path("movies/<int:pk>/", movie_object, name="movie-list")
]

app_name = "cinema"
