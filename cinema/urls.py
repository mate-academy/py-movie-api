from django.urls import path

from cinema.views import movies_list, movie_list

urlpatterns = [
    path("movies/", movies_list, name="movies-list"),
    path("movies/<int:pk>/", movie_list, name="movie-list"),
]

app_name = "cinema"
