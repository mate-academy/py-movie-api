from django.urls import path

from .views import cinema_list, cinema_detail

urlpatterns = [
    path("movies/", cinema_list, name="movies-list"),
    path("movies/<int:pk>/", cinema_detail, name="movie-detail"),
]
app_name = "cinema"
