from django.urls import path

from cinema.views import movies_list, movie_detail


app_name = "cinema"

urlpatterns = [
    path("cinema/movies/", movies_list, name="movies_list"),
    path("cinema/movies/<int:pk>/", movie_detail, name="movie_detail"),
]
