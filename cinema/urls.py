from django.urls import path

from cinema.views import movie_list, movie_item

urlpatterns = [
    path("movies/", movie_list, name="movie-list"),
    path("movies/<pk>/", movie_item, name="movie-item")
]

app_name = "cinema"
