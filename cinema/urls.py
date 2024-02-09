from django.urls import path

from .views import MovieListView, MovieDetailView

urlpatterns = [
    path("movies/",
         MovieListView,
         name="movie-list"),
    path("movies/<pk>/",
         MovieDetailView,
         name="movie-detail")
]

app_name = "cinema"
