from django.urls import path

from cinema.views import cinema_list, certain_movie

urlpatterns = [
    path("movies/", cinema_list, name="movie-list"),
    path("movies/<pk>/", certain_movie, name="certain-movie"),
]

app_name = "cinema"
