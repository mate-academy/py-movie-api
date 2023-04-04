from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.movie_list, name='movie_list'),
    path('movies/<int:pk>/', views.movie_detail, name='movie_detail'),
]

app_name = 'cinema'
