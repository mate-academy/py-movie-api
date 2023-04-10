from django.urls import path

from .views import (
    movie_list,
    movie_datail
)

urlpatterns = [
    path("home/", movie_list, name="movies"),
    path("home/<int:pk>/", movie_datail, name="movie"),
]

app_name = "cinema"
