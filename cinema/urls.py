from django.urls import path

from cinema.views import movie_list_view, movie_detail_view

urlpatterns = [
    path("cinema/movies/", movie_list_view, name="movie_list"),
    path("cinema/movies/<int:pk>/", movie_detail_view, name="movie_detail")
]

app_name = "cinema"
