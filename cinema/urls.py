from django.urls import path
from cinema.views import movie_list, movie_id

urlpatterns = [
    path("movies/", movie_list, name="movie_list"),
    path("movies/<int:pk>/", movie_id, name="movie_id"),
]

app_name = "cinema"
