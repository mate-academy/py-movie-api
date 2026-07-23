from django.urls import path

from cinema.views import movie_detail, movie_list

app_name = "movies"

urlpatterns = [
    path("movies/", movie_list, name="movie_list"),
    path("movies/<pk>/", movie_detail, name="movie_detail"),
]
