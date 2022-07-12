from django.urls import path

from cinema.views import movie_view, movie_detail

urlpatterns = [
    path("movies/", movie_view, name="movie_view"),
    path("movies/<int:pk>/", movie_detail, name="movie-detail")
]

app_name = "cinema"
