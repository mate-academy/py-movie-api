from django.urls import path

from .views import movies_list, movie

urlpatterns = [
    path("movies/", movies_list, name="movie-list"),
    path("movies/<int:pk>/", movie, name="movie-delete-update-get"),
]

app_name = "cinema"
