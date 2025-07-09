from django.urls import path
from .views import MovieListCreateAPIView, MovieRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('movies/', MovieListCreateAPIView.as_view(), name='movie-list'),
    path('movies/<int:pk>/', MovieRetrieveUpdateDestroyAPIView.as_view(), name='movie-detail'),
]
