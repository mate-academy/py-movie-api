from django.urls import path
from cinema.views import movie_list_detail, movie_list

urlpatterns = [
    path("movies/",  movie_list, name="movie-list"),
    path("movies/<pk>/", movie_list_detail, name="movie-list-detail"),

]

app_name = "cinema"
