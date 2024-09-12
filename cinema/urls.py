from django.urls import path

from cinema.views import movies_list, movies_detail

urlpatterns = [
    path("movies/", movies_list, name="movie-list"),
    path("movies/<pk>/", movies_detail, name="movie-detail"),
]

app_name = "cinema"
