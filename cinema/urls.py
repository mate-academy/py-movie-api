from django.urls import path
from . import views

urlpatterns = [
    path(
        "api/cinema/movies/",
        views.MovieListCreateView.as_view(),
        name='movie-list-create'
    ),
    path(
        "api/cinema/movies/<int:pk>/",
        views.MovieRetrieveUpdateDeleteView.as_view(),
        name="movie-detail"
    ),
]
