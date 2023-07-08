from django.urls import path, include

from cinema.views import movie_list, movie_detail

urlpatterns = [
    path("cinemas/", movie_list, name="cinema-list"),
    path("movies/<int:pk>/", movie_detail, name="movie-detail"),
]

app_name = "cinema"
