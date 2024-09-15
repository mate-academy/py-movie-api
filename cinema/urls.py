from django.urls import path

from cinema.views import movies_list, movie_update

urlpatterns = [
    path("movies/", movies_list, name="movies-list"),
    path("movies/<int:pk>/", movie_update, name="movie-update"),
]

app_name = "cinema"
