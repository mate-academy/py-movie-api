from django.urls import path

from cinema.views import MovieListView, MovieDetailView

app_name = "cinema"

urlpatterns = [
    path(
        "movies/",
        MovieListView.as_view(),
        name="movie_list"
    ),
    path(
        "movies/<int:pk>/",
        MovieDetailView.as_view(),
        name="movie_detail"
    ),
]
