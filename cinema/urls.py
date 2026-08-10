from django.urls import path

from cinema.views import movie_list, moive_detail

urlpatterns = [
    path("movies/", movie_list, name="movie-list"),
    path("movies/<int:pk>/", moive_detail, name="moive-detail"),
]

app_name = "cinema"
