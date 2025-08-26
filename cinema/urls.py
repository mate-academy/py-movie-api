from django.urls import path
from . import views

urlpatterns = [
    path('api/cinema/movies/', views.movie_list, name='movie-list'),
    path('api/cinema/movies/<int:pk>/', views.movie_detail, name='movie-detail'),
]
