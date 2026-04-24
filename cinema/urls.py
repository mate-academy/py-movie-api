from django.urls import path

from .views import MovieListView, MovieDetailView

app_name = "cinema"

urlpatterns = [
    path("movies/", MovieListView.as_view(), name="movie-list"),
    path("movies/<int:pk>/", MovieDetailView.as_view(), name="movie-detail"),
]


