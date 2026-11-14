from django.urls import path

from cinema import views

app_name = "cinema"

urlpatterns = [
    path("movies/", views.cinema_list, name="cinema_list"),
    path("movies/<int:pk>/", views.cinema_detail, name="cinema_detail"),
]
