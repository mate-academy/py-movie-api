from django.urls import path

from cinema.views import MovieList, MovieDetail

urlpatterns = [
    path("", MovieList.as_view(), name="movie-list"),
    path("<int:pk>/", MovieDetail.as_view(), name="movie-detail"),
]

app_name = "cinema"
