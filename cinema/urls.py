from django.urls import path
from .views import movies_list_view, movie_detail_view


urlpatterns = [
    path("api/cinema/movies/", movies_list_view, name="movies-list"),
    path("api/cinema/movies/<int:pk>/", movie_detail_view, name="movie-detail"),
]

app_name = "cinema"
