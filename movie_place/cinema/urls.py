from django.urls import path

from .views import cinema_list, cinema_detail

app_name = 'cinema'

urlpatterns = [
    path('api/cinema/movies/', cinema_list, name='cinema_list'),
    path('api/cinema/movies/<int:pk>/', cinema_detail, name='cinema_detail'),
]