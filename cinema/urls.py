from django.urls import path
from . import views

app_name = "cinema"

urlpatterns = [
    path("movies/", views.movie_list, name="movie-list"),
    path("movies/<int:pk>/", views.movie_detail, name="movie-detail"),
]
