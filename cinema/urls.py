from django.urls import path
from .views import movie_list, movie_detail

app_name = "cinema"

urlpatterns = [
    path("cinema/movies/", movie_list, name="movie_list"),
    path("cinema/movies/<int:pk>/", movie_detail, name="movie_detail")
]
