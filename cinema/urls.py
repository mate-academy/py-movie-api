from django.urls import path
from cinema.views import movies_detail, movies_list


urlpatterns = [
    path("movies/", movies_list, name="movies_list"),
    path("movies/<pk>/", movies_detail, name="movies_detail"),
]

app_name = "cinema"
