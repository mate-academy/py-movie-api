from django.urls import path

from .views import MovieDetailView, MovieListCreateView


urlpatterns = [
    path("movies/", MovieListCreateView.as_view()),
    path("movies/<int:pk>/", MovieDetailView.as_view()),
]
