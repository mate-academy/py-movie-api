from django.urls import path

from cinema.views import movie_detail, movie_list


urlpatterns = [
    path('movies/', movie_list, name='movie-list'),
    path('movies/<int:pk>/', movie_detail, name='movie-detail'),
]
