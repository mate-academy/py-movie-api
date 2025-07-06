from django.urls import path
from .views import cinema_detail, cinema_list

app_name = "cinema"

urlpatterns = [
    path("movies/", cinema_list, name="cinema_list"),
    path("movies/<int:pk>/", cinema_detail, name="cinema_detail"),
]
