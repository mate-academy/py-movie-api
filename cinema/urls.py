from django.urls import path
from .views import MovieList, MovieDetail

urlpatterns = [
    path('movies/', MovieList.as_view(), name='movie_list'),
    path('movies/<int:pk>/', MovieDetail.as_view(), name='movie_detail'),
]
