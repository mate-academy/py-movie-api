from django.urls import path

from cinema.views import movie_list, movie_detail

urlpatterns = [
    path("api/cinema/movies/", movie_list, name="movie-list"),
    path("api/cinema/movies/<int:pk>/", movie_detail, name="movie-detail"),
    path("api/cinema/movies/", movie_list, name="movie-create"),
    path("api/cinema/movies/<int:pk>/", movie_detail, name="movie-update"),
    path("api/cinema/movies/<int:pk>/", movie_detail, name="movie-delete"),
]

app_name = "cinema"
