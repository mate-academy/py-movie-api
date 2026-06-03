from django.urls import path
from cinema.views import (
    cinema_list,
    cinema_detail,
)

app_name = 'cinema'

urlpatterns = [
    path("api/cinema/movies/", cinema_list, name="cinema_list"),
    path("api/cinema/movies/<pk>/", cinema_detail, name="cinema_delete"),
]
