from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from cinema import views

urlpatterns = [
    path("api/cinema/movies/", views.movie_list),
    path("api/cinema/movies/<int:pk>/", views.movie_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)

app_name = "cinema"
