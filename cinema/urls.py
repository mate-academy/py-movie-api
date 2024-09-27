from django.urls import path

from cinema.views import get_movie_list, get_movie_by_id

urlpatterns = [
    path("movies/", get_movie_list, name="movie_list"),
    path("movies/<int:pk>/", get_movie_by_id, name="movie_info"),
]

app_name = "cinema"
