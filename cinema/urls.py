from cinema.views import movies_list, movie_detail
from django.urls import path

urlpatterns = [
    path("movies/", movies_list, name="movies-list"),
    path("movies/<pk:int>/", movie_detail, name="movie-detail"),
]

app_name = "movies"
