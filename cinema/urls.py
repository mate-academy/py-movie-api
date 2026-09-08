from django.urls import path

from cinema.views import movie_detail, movie_list

urlpatterns = [
    path("movies/<int:pk>/", movie_detail, name="movie_detail"),
    path("movies/", movie_list, name="movie_list"),
]


app_name = "cinema"
