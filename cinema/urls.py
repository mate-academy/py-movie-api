from django.urls import path

from cinema.views import movie_list, movie_detail

urlpatterns = [
    path("movies/", movie_list, name="movi-list"),
    path("movies/<int:pk>/", movie_detail, name="movi-detail"),
]

app_name = "cinema"
