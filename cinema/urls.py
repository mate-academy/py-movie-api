from django.urls import path

from cinema.views import MoviesList, MovieDetail

app_name = "cinema"


urlpatterns = [
    path("movies/", MoviesList.as_view(), name="movies-list"),
    path("movies/<int:pk>/", MovieDetail.as_view(), name="movie-detail"),
]
