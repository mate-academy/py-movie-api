from django.urls import path

from .views import (
    cinema_list,
    ciname_datail
)

urlpatterns = [
    path("home/", cinema_list, name="cinema-list"),
    path("home/<int:pk>/", ciname_datail, name="cinema-detail"),
]

app_name = "cinema"