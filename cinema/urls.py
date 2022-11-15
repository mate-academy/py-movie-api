from django.urls import path

urlpatterns = [
    path(
        "movies/",
        movie_list,
        name="movies-list"
    )
]

app_name = "cinema"
