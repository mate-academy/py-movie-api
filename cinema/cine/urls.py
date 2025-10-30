from django.urls import path
from .views import cinema_detail, cinema_list

app_name = "cine"

urlpatterns = [
    path("cine/", cinema_list, name="cinema_list"),
    path("cine/<int:pk>/", cinema_detail, name="cinema_detail"),
]