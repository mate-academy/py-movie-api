from django.urls import path

from cinema.views import movie_list, movie_id

urlpatterns = [
    path("movies/", movie_list, name="movie-list"),
    path("movies/<int:pk>", movie_id, name="movie-id")

]

app_name = "cinema"
