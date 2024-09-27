from django.urls import path
from cinema.views import movie_list, movie_detail


urlpatterns = [
    path("movies/", movie_list, name="movie-list"),
    path("movie/<int:pk>/", movie_detail, name="moview-detail")
]


app_name = "cinema"
