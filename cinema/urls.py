from django.urls import path

from cinema.views import movie_list, movie_detail

urlpatterns = [
    path("movies/", movie_list, name="cinema-list"),
    path("movies/<pk>", movie_detail, name="cinema-object"),
]

app_name = "cinema"
