from django.urls import path
from movieapi.cinema.views import MovieList, MovieDetail

app_name = "cinema"

urlpatterns = [
    path('movies/', MovieList.as_view()),
    path('movies/<int:pk>/', MovieDetail.as_view()),
]
