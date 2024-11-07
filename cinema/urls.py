from django.urls import path
from cinema.views import movie_list, movie_detail


app_name = 'cinema'

urlpatterns = [
    path('api/cinema/movies/', movie_list, name='movie-list'),
    path('api/cinema/movies/<int:pk>/', movie_detail, name='movie-detail'),
]