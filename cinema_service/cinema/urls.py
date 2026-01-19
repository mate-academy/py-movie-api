from django.urls import path
from cinema.views import (
    MovieListCreateView,
    MovieRetrieveUpdateDestroyView,
)

urlpatterns = [
    path("movies/", MovieListCreateView.as_view(), name="movie-list"),
    path("movies/<int:pk>/", MovieRetrieveUpdateDestroyView.as_view(), name="movie-detail"),
]

app_name = "cinema"
