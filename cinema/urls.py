from django.urls import path

from cinema.views import movie_list, movie_detailed

urlpatterns = [
    path("movies/", movie_list, name="movie_list"),
    path("movies/<pk>/", movie_detailed, name="movie_detailed"),
]

app_name = "cinema"
