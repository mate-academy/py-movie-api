from django.urls import path

from cinema.views import movie_list

urlpatterns = [
    path(
        "movies/",
        movie_list,
        name="movies-list"
    )
]

app_name = "cinema"
