from django.urls import path

from .views import movie_list, movie_detail

urlpatterns = [
    path("movies/", movie_list, name="movies_list"),
    path("movies/<int:pk>/", movie_detail, name="movies_detail"),
]
