from django.urls import path
from cinema import views

app_name = "cinema"

urlpatterns = [
    path("buses/", views.movie_list, name="movie_list"),
    path("buses/<int:movie_pk/>", views.movie_detail, name="movie_detail"),
]