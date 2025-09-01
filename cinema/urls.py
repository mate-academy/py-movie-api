from django.urls import path
from cinema.views import movie_list_create, movie_detail


app_name = "cinema"

urlpatterns = [
    path("movies/", movie_list_create, name="movie-list-create"),
    path("movies/<int:pk>/", movie_detail, name="movie-detail"),
]
