from django.urls import path

from cinema.views import movies_get_or_create, movie_get_update_delete


app_name = "cinema"

urlpatterns = [
    path("movies/", movies_get_or_create, name="movie-list"),
    path("movies/<int:pk>/", movie_get_update_delete, name="movie-detail"),
]