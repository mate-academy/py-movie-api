from django.urls import path

from cinema.views import movie_detail, movie_list

app_name = "cinema"

urlpatterns = [
    path("api/v1/movies/", movie_list, name="movie_list"),
    path("api/v1/movies/<int:pk>/", movie_detail, name="movie_detail"),
]
