from django.urls import path

from cinema.views import movies_list, movie

urlpatterns = [
    path("movies/", movies_list, name="movies-list"),
    path("movies/<int:pk>/", movie, name="movie")
]

app_name = "station"
