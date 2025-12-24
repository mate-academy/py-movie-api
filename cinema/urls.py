from django.urls import path
from cinema.views import MovieListCreateView, MovieDetailView

urlpatterns = [
    path("movies/", MovieListCreateView.as_view()),
    path("movies/<int:pk>/", MovieDetailView.as_view()),
]
