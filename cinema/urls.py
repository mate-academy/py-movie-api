from django.urls import path
from cinema.views import MovieListCreateView, MovieRetrieveUpdateDestroyView

urlpatterns = [
    path(
        "cinema/movies/",
        MovieListCreateView.as_view(),
        name="movie-list-create"
    ),
    path(
        "movies/<int:pk>/",
        MovieRetrieveUpdateDestroyView.as_view(),
        name="movie-retrieve-update-destroy"
    ),
]

app_name = "cinema"
