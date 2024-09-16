from django.urls import path

from cinema.views import movie_list, movie_update

urlpatterns = [
    path("movies/", movie_list, name="movies-list"),
    path("movies/<int:pk>/", movie_update, name="movies-update"),
]

app_name = "cinema"
