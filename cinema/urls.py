from django.urls import path

from cinema.views import movie_list, movie

urlpatterns = [
    path("api/cinema/movies/", movie_list, name="movie_list"),
    path("api/cinema/movies/<pk>/", movie, name="movie"),

]

app_name = "cinema"
