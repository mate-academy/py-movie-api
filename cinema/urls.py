from django.urls import path

from cinema.views import movie_list, movie_detail_view

urlpatterns = [
    path("movies/", movie_list, name="movies-list"),
    path("movies/<int:pk>/", movie_detail_view, name="movie-detail"),
]

app_name = "cinema"
