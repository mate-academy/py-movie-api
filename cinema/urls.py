from django.urls import path

from cinema.views import cinema_list, movie_detail

app_name = "cinema"

urlpatterns = [
    path("movies/", cinema_list, name="cinema_list"),
    path("movies/<int:pk>/", movie_detail, name="cinema_detail"),
]
