from django.urls import path

from cinema.views import MovieListAPIView, MovieDetailAPIView


app_name = "cinema"

urlpatterns = [
    path(
        "movies/",
        MovieListAPIView.as_view(),
        name="movie_list"
    ),
    path(
        "movies/<int:pk>/",
        MovieDetailAPIView.as_view(),
        name="movie_detail"
    )
]
