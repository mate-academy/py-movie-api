from django.urls import path

from cinema.views import movies_list, movie_detail_view

urlpatterns = [
    path("movies/", movies_list, name="movies-list"),
    path("movies/<int:pk>", movie_detail_view, name="movie-detail"),
]

app_name = "cinema"
