from django.urls import path
from cinema.views import movies_list, movies_detail

app_name = "cinema"

urlpatterns = [
    path("movies/", movies_list, name="movies-list"),
    path("movies/<int:pk>/", movies_detail, name="movies-detail"),
]
