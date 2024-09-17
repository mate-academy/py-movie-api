from django.urls import path

from cinema.views import movies_list, movie_by_id

urlpatterns = [
    path('movies/', movies_list, name="movie-list"),
    path('movies/<int:pk>/', movie_by_id, name="movie"),

]

app_name = "cinema"
