from django.urls import path

from cinema.views import movie_list, movie_detail

urlpatterns = [
    path("movies/", movie_list),
    path("movies/<int:pk>/", movie_detail),
]

app_name = "cinema"
