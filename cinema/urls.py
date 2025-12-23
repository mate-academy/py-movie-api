from django.urls import path

from .views import MovieListCreateView, MovieDetailView


urlpatterns = [
    path("movies/", MovieListCreateView.as_view()),
    path("movies/<int:pk>/", MovieDetailView.as_view()),
]
