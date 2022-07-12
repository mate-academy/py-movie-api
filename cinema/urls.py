from django.urls import path

from cinema.views import movie_view

urlpatterns = [
    path("/movies/", movie_view, name="movie"),
    path("/movies/<int:pk>/", movie_view, name="movie")
]

app_name = "cinema"
