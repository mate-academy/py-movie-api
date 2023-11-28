from django.urls import path

from cinema.views import movie_list, movie_pk_list

urlpatterns = [
    path("movies/", movie_list, name="movie-list"),
    path("movies/<int:pk>/", movie_pk_list, name="movie-pk-list"),
]

app_name = "cinema"
