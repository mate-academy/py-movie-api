from django.urls import path

from cinema.views import movies, movie_detail

urlpatterns = [
    path("movies/", movies, name="movies"),
    path("movies/<int:pk>/", movie_detail, name="movies-detail"),
]


app_name = "cinema"
