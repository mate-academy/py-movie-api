from django.urls import path
from movie_project.cinema import views


urlpatterns = [
    path("api/cinema/movies/", views.movie_list, name="movie_list"),
    path("api/cinema/movies/<int:pk>/", views.movie_list, name="movie_detail"),
]
