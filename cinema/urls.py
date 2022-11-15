from django.urls import path

from cinema.views import movies_list, movies_update

urlpatterns = [
    path("movies/", movies_list, name="movies-list"),
    path("movies/<int:pk>/", movies_update, name="movies-update"),
]

app_name = "cinema"
