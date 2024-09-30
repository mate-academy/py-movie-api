from django.urls import path

from cinema.views import movies, movie_details


app_name = 'cinema'

urlpatterns = [
    path("movies/", movies, name="movies"),
    path("movies/<int:pk>/", movie_details, name="movie_details"),
]
