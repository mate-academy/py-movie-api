from django.urls import path
from cinema import views

urlpatterns = [
    path("cinema/movies/", views.cinema_list, name="cinema-list"),
    path("cinema/movies/<int:pk>/", views.cinema_detail, name="cinema-detail"),
]

app_name = "cinema"
