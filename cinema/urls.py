from django.urls import path
from .models import Movie
from .views import (
    movies_list,
    movies_detail
)

urlpatterns = [
    path("movies/", movies_list, name="movies_list"),
    path("movies/<int:movie_id>/", movies_detail, name="movies_list"),
]

app_name = "cinema"
