from django.contrib import admin
from django.urls import path, include

import cinema
from cinema.views import cinema_list, cinema_retrieve

urlpatterns = [
    path("api/cinema/movies/", cinema_list),
    path("api/cinema/movies/<int:pk>", cinema_retrieve),
]
app_name = "api"
