from django.urls import path

from cinema.views import MovieListCreate, MovieRetrieveUpdateDelete

app_name = "cinema"

urlpatterns = [
    path("movies/", MovieListCreate.as_view(), name="movie-list-create"),
    path(
        "movies/<int:pk>/", MovieRetrieveUpdateDelete.as_view(), name="movie-detail-rud"
    ),
]
