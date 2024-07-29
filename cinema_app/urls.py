from django.urls import path
from cinema_app.views import movie_list, movie_detail

urlpatterns = [
    path("movies/", movie_list, name="movie_list"),
    path("movies/<int:pk>/", movie_detail, name="movie_detail"),
]

app_name = "cinema"
