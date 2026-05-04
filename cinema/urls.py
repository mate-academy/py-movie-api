from django.urls import path
from cinema.views import movie_list, movie_detail

urlpatterns = [
    path("", movie_list, name="movie_list"),
    path("<int:pk>/", movie_detail, name="movie_detail"),
]

app_name = "cinema"
