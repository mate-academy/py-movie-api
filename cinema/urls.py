from django.urls import path
from cinema.views import movies_list, movie_detail

app_name = 'cinema'

urlpatterns = [
    path('cinema/movies/', movies_list, name='movies-list'),
    path('cinema/movies/<int:movie_id>', movie_detail, name='movies-detail'),
]
