from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from cinema.views import movie_list, movie_detail


urlpatterns = [
    path("movies/", movie_list, name="movie-list"),
    path("movies/<int:pk>/", movie_detail, name="movie-detail"),
]

app_name = "cinema"

urlpatterns = format_suffix_patterns(urlpatterns)
