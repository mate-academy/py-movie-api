from django.urls import path

from cinema.views import movies_list, detail_movie

urlpatterns = [
    path("movies/", movies_list, name="movies-list"),
    path("movies/<int:pk>/", detail_movie, name="detail-movie"),
]

app_name = "cinema"
