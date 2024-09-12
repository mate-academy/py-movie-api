
from django.urls import path

from .views import movie_list, movie_one

urlpatterns = [
    path("cinema/movies/", movie_list, name="movie_list"),
    path('cinema/movies/<int:pk>', movie_one, name="movie_one")
]

app_name = "cinema"
