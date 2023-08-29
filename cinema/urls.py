from django.urls import path
from cinema.views import movie_list_create, get_update_movie

urlpatterns = [
    path("movies/", movie_list_create, name="movie_list_create"),
    path("movies/<int:pk>/", get_update_movie, name="get_update_movie")
]

app_name = "cinema"
