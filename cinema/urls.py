from django.urls import path

from cinema.views import movie_get_post, movie_get_put_delete

app_name = "cinema"

urlpatterns = [
    path("movies/", movie_get_post, name="movie-list"),
    path("movies/<int:pk>/", movie_get_put_delete, name="movie-detail"),
]
