from django.urls import path

from cinema.views import movies_list


app_name = "cinema"
urlpatterns = [
    path("movies/", movies_list, name="movies-list"),
]