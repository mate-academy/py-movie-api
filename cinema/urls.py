from django.urls import path
from cinema.views import movie_list, movie_detail

urlpatterns = [
    path('cinema/movies/', movie_list, name="movie_list"),
    path('cinema/movies/<int:movie_id>/', movie_detail, name="movie_detail"),
]

app_name = "cinema"
