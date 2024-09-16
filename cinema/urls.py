from django.urls import path

from .views import movies_list, one_movie


urlpatterns = [
    path("movies/", movies_list, name="movie_list"),
    path('movies/<int:pk>', one_movie, name="one_movie")
]

app_name = "cinema"
