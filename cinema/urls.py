from django.urls import path

from cinema.views import movie_list, movie_detail

urlpatterns = [
    path("movies/", movie_list.as_view(), name="movie-list"),
    path("movies/<int:pk>/", movie_detail.as_view(), name="movie-detail"),
]

app_name = "cinema"
