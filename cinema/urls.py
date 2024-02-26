from django.urls import path

from cinema.views import movie_list, movie_detail

urlpatterns = [
    path("movies/", movie_list, name="movies"),
    path("movies/<int:pk>/", movie_detail, name="movie_detail"),
]

app_name = "cinema"
