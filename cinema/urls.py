from django.urls import path

from cinema.views import (
    cinema_list_view,
    cinema_detail_view
)

app_name = "cinema"

urlpatterns = [
    path("movies/", cinema_list_view, name="cinema_list"),
    path("movies/<int:pk>/", cinema_detail_view, name="cinema_detail")
]
