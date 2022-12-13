from django.urls import path

from cinema.views import movie_list, movie_detail

urlpatterns = [
    path("api/cinema/movies/", movie_list, name="film_list"),
    path("api/cinema/movies/<int:pk>/", movie_detail, name="film_detail"),
]

app_name = "cinema"
