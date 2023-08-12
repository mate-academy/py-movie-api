from django.urls import path
from cinema.views import movie_list

urlpatterns = [
    path("movies/", movie_list, name="movie-list"),
    # path

]

app_name = "cinema"
