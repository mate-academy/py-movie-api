from django.urls import path
from cinema.views import movie_list_create

urlpatterns = [
    path("movies/", movie_list_create, name="movie_list_create"),
]

app_name = "cinema"
