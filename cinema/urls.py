from django.urls import path

from cinema import views

urlpatterns = [
    path('movies/', views.movies_view, name='movies'),
    path('movies/<int:pk>/', views.movie_detail, name='movie_detail')
]

app_name = 'cinema'

