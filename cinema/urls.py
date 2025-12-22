from django.urls import path

from cinema.views import movie_detail, movie_list

app_name = "cinema"

urlpatterns = [
    path("api/cinema/movies/", movie_list, name="movie_list"),
    path("api/cinema/movies/<int:pk>/", movie_detail, name="movie_detail"),
]
