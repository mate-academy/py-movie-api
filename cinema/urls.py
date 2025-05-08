from django.urls import path
from . import views


app_name = "cinema"

urlpatterns = [
    path("movies/", views.movie_list_create, name="movie_list_create"),
    path(
        "movies/<int:pk>/",
        views.movie_detail_get_update_delete, name="movie_detail"),
]
