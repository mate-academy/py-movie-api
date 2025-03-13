from django.urls import path
from cinema.views import movie_detail, movies_list

app_name = "cinema"

urlpatterns = [
    path("movies/", movies_list, name="movie_list"),
    path("movies/<int:pk>/", movie_detail, name="movie_detail"),
]
