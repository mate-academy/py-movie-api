from django.urls import path

from cinema.views import movies_list, movie_item

urlpatterns = [
    path("movies/", movies_list, name="movies-list"),
    path("movies/<pk>/", movie_item, name="movie-item"),
]
app_name = "cinema"
