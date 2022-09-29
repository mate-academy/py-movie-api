from django.urls import path

from cinema.views import cinema_create, cinema_get_put_delete

urlpatterns = [
    path("api/cinema/movies/<int:pk>/", cinema_get_put_delete, name="cinema-GET-PUT-DELETE"),
    path("api/cinema/movies/", cinema_create, name="cinema-POST"),
]

app_name = "cinema"
