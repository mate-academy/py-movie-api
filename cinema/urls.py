"""URL routes for cinema API resources."""

from __future__ import annotations

from django.urls import path

from cinema.views import MovieListCreateView, MovieRetrieveUpdateDestroyView

urlpatterns = [
    path("movies/", MovieListCreateView.as_view(), name="movie-list-create"),
    path("movies/<int:pk>/", MovieRetrieveUpdateDestroyView.as_view(), name="movie-detail"),
]
