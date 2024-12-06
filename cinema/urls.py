from django.urls import path

from cinema.views import list_movie, detail_movie

app_name = "cinema"
urlpatterns = [
    path("cinema/movies/", list_movie, name="list_movie"),
    path(
        "cinema/movies/<int:pk>/",
        detail_movie,
        name="detail_movie",
    ),
]
