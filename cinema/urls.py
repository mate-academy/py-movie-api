from django.urls import path,
from .views import movie_detail, movie_list


urlpatterns = [
    path("api/cinema/movies/", movie_list, name="movie-list"),
    path("api/cinema/movies/<int:pk>/", movie_detail, name="movie-detail"),
]
