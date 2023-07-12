from django.urls import path

from cinema.views import movie_adjust, movie_list

urlpatterns = [
    path("movies/", movie_list, name="movie-list"),
    path("movies/<int:pk>/", movie_adjust, name="movie-detail"),
]
app_name = "cinema"
