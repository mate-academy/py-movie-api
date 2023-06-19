from django.urls import path
from cinema.views import movie_list

urlpatterns = [
    path("movie/", movie_list, name="movie_list")
]

app_name = "cinema"
