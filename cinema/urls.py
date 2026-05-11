from django.urls import path

from .view import cinema_list, cinema_detail

app_name = 'cinema'

urlpatterns = [
    path('cinemas/', cinema_list, name='cinema_list'),
    path('cinema/<int:pk>/', cinema_detail, name='cinema_detail'),
]
