from django.urls import path

from cinema.views import cinema_list

urlpatterns = [
    path("movies/", cinema_list, name="movie_list")
]

app_name = "cinema"