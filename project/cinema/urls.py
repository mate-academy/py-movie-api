from django.urls import path

from cinema.views import (
    movies_list,
    movies_detail,
)

app_name = "cinema"

urlpatterns = [
    path("api/cinema/movies/", movies_list),
    path("api/cinema/movies/<int:pk>/", movies_detail),
    path("api/cinema/movies/", movies_list),
    path("api/cinema/movies/<int:pk>/", movies_detail),
    path("api/cinema/movies/<int:pk>/", movies_detail),
]
