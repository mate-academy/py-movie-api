from django.urls import path

from cinema.views import cinema_create

urlpatterns = [
    path("movies/<int:pk>/", cinema_detail, name="cinema-GET-PUT-DELETE"),
    path("movies/", cinema_create, name="cinema-POST"),
]

app_name = "cinema"
