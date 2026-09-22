from django.urls import path

from cinema.views import MovieDetailView, MovieListCreateView


urlpatterns = [
    path("movies/", MovieListCreateView.as_view(), name="movie-list"),
    path("movies/<int:pk>/", MovieDetailView.as_view(), name="movie-detail"),
]