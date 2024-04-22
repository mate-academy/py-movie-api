from django.urls import path
from cinema.views import get_list, get_detail


urlpatterns = [
    path("movies/", get_list, name="movie_list"),
    path("movies/<int:pk>", get_detail, name="movie_detail")
]

app_name = "cinema"
