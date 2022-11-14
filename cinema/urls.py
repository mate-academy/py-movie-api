from django.urls import path

from cinema.views import movie_list, movie_element

urlpatterns = [
    path("movies/", movie_list, name="movies-list"),
    path("movies/<int:pk>/", movie_element, name="movie-element"),
]

app_name = "cinema"
