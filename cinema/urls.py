from django.urls import path

from cinema.views import cinema_create

urlpatterns = [
    path("movies/<int:pk>/", cinema_create, name="cinema-GET-PUT-DELETE"),
    path("api/cinema/movies/", cinema_create, name="cinema-POST"),
]

app_name = "cinema"
