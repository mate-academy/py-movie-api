from django.urls import path

from .views import MovieListCreateView, MovieRetrieveUpdateDestroyView



urlpatterns = [
    path("movies/", MovieListCreateView.as_view(), name="movie-list-create"),
    path("movies/<int:pk>/", MovieRetrieveUpdateDestroyView.as_view(), name="movie-detail")
]
