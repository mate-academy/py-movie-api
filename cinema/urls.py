from django.urls import path

from .views import movie_list_view, movie_detail_view


urlpatterns = [
    path("movies/", movie_list_view, name="cinema-list"),
    path("movies/<int:pk>/", movie_detail_view, name="cinema-detail"),
]

app_name = "cinema"
