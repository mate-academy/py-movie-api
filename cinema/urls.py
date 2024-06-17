from django.urls import path
from .views import cinema_list, cinema_detail

app_name = "movies"

urlpatterns = [
    path("movies/", cinema_list, name="cinema_list"),
    path("movies/<int:pk>/", cinema_detail, name="cinema_detail")

]
