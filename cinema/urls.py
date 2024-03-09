from django.urls import path

from cinema.views import movie_detail_view, movie_list_view

urlpatterns = [
    path("movies/", movie_list_view, name="movie_list"),
    path("movies/<int:pk>/", movie_detail_view, name="movie_detail")
]

app_name = "cinema"
