from django.urls import path

from cinema.views import movies_list_create, movies_detail


urlpatterns = [
    path("cinema/movies/", movies_list_create, name="movies_list"),
    path("cinema/movies/<int:pk>/", movies_detail, name="movies_detail"),
]

app_name = "movies"
