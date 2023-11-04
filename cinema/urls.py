from django.urls import path
from cinema.views import movie_list, movie_list_detail, movie_list_update, movie_delete

urlpatterns = [
    path("movies/", movie_list, name="movie-list"),
    path("movies/<pk>/", movie_list_detail, name="movie-list-detail"),
    path("movies/<pk>/", movie_list_update, name="movie-list-update"),
    path("movies/<pk>/", movie_delete, name="movi-delete"),
]

app_name = "cinema"
