from django.urls import path

from cinema.views import MovieViewSet

app_name = "cinema"

movie_list = MovieViewSet.as_view({
    "get": "list",
    "post": "create"
})

movie_detail = MovieViewSet.as_view({
    "get": "retrieve",
    "put": "update",
    "delete": "destroy"
})

urlpatterns = [
    path("movies/", movie_list, name="movie-list"),
    path("movies/<int:pk>/", movie_detail, name="movie-detail"),
]
