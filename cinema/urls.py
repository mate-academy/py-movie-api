from django.urls import path
from cinema.views import movie_list, movie_detail, movie_create, movie_update, movie_delete


urlpatterns = [
    path("movies/", movie_list, name="movie_list"),
    path("movies/<int:pk>/", movie_detail, name="movie_detail"),
    path("movies/create/", movie_create, name="movie_create"),
    path("movies/<int:pk>/update/", movie_update, name="movie_update"),
    path("movies/<int:pk>/delete/", movie_delete, name="movie_delete"),
]

app_name = "cinema"
