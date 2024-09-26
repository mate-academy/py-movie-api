from django.urls import path

from .views import movie_detail, movies_list

urlpatterns = [
    path("movies/", movies_list, name="movies"),
    path("movies/<int:pk>/", movie_detail, name="movie"),
]

app_name = "cinema"
