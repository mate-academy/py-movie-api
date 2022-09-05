from django.urls import path

from cinema.views import (
    cinema_list_view,
    cinema_detail_view
)

urlpatterns = [
    path("cinema/movies/", cinema_list_view, name="cinema-list"),
    path("cinema/movies/<int:pk>/", cinema_detail_view, name="cinema-detail")

]

app_name = "cinema"
