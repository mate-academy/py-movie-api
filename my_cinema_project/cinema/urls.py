from django.urls import path

from cinema.views import movie_view

urlpatterns = [
    path("movies/", movie_view, name="movie-list"),
    path("movies/<int:pk>/", movie_view, name="movie-detail"),
]

app_name = "cinema"
