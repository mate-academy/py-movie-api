from django.urls import path
from . import views

urlpatterns = [

    path("movies/", views.movie_list, name="movie-list"),
    path("movies/", views.movie_create, name="movie-create"),

    # Retrieve, update, or delete a single movie by ID
    path("movies/<int:pk>/", views.movie_detail, name="movie-detail"),
    path("movies/<int:pk>/", views.movie_update, name="movie-update"),
    path("movies/<int:pk>/", views.movie_delete, name="movie-delete"),
]
