from django.urls import path
from .views import movie_list, movie_detail

urlpatterns = [
    path("movies/", movie_list, name="movie-list-create"),
    path("movies/<int:pk>/", movie_detail, name="movie-detail"),
]
