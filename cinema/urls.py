from django.urls import path
from cinema.views import movie_detail, movie_list


app_name = "cinema"

urlpatterns = [
    path("", movie_list, name="movie_list"),

    path("movie/<int:id>", movie_detail, name="movie_detail"),
]
