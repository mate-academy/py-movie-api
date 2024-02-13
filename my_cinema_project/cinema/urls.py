from django.urls import path

from cinema.views import movie_view

urlpatterns = [
    path("movies/", movie_view, name="movie-list"),
    path("movies/<int:pk>/", movie_view, name="movie-update"),
    path("movies/<int:pk>/", movie_view, name="movie-detail"),
    path("movies/", movie_view, name="movie-create"),
    path("movies/<int:pk>/", movie_view, name="movie-delete")
]

app_name = "cinema"
