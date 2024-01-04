from django.urls import path
from cinema.views import get_all_movies, movie_detail

urlpatterns = [
    path("movies/", get_all_movies),
    path("movies/<int:pk>/", movie_detail)
]
