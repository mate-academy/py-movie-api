from django.urls import path

from .views import movie_list, movie_detail

urlpatterns = [
    path("movie/", movie_list, name="movie-list"),
    path("movie/<int:pk>/", movie_detail, name="movie_detail"),
]

app_name = "cinema"
