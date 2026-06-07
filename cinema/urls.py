from django.urls import path
from cinema.views import movielist, moviedetail

urlpatterns = [
    path("movies/", movielist, name="movie-list"),
    path("movies/<int:pk>/", moviedetail, name="movie-detail"),
]

app_name = "cinema"
