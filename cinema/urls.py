from django.urls import path

from .views import movie_list, movie_list

urlpatterns = [
    path("movies/",
         movie_list,
         name="movie-list"),
    path("movies/<pk>/",
         movie_list,
         name="movie-detail")
]

app_name = "cinema"
