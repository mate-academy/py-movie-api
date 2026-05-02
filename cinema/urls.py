from django.urls import path

from cinema.views import cinema_detail, cinema_list

urlpatterns = [
    path("movies/", cinema_list, name="cinema_list"),
    path("movies/<int:pk>/", cinema_detail, name="cinema_detail"),
]
