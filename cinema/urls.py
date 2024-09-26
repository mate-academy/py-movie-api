from django.urls import path

from .views import (
    cinema_list,
    cinema_detail,
)


urlpatterns = [
    path("movies/", cinema_list, name="cinema-list"),
    path("movies/<pk>/", cinema_detail, name="cinema-detail"),
]

app_name = "cinema"
