from django.urls import path

from cinema import views

urlpatterns = [
    path("movies/", views.movie_list, name="movies-list"),
    # path("movies/<pk>/"),
]

app_name = "cinema"
