from django.urls import path

from cinema.views import cinema_list_view, cinema_detail_view

urlpatterns = [
    path("movies/", cinema_list_view, name="movies"),
    path("movies/<int:pk>/", cinema_detail_view, name="movie-detail"),
]

app_name = "cinema"
