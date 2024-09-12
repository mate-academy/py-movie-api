from django.urls import path
from movie_project.cinema import views


urlpatterns = [
    path("/movies/", views.movie_list, name="movie_list"),
    path("/movies/<int:pk>/", views.movie_list, name="movie_detail"),
]
