from django.urls import path

from cinema.views import movie_list

urlpatterns = [
    path("movies/", movie_list, name="config-list"),
    path("movies/<int:pk>/", movie_list, name="config-list"),
]

app_name = "cinema"
