from django.urls import path

from cinema.views import movies_list, movies_list_by_id

app_name = 'cinema'

urlpatterns = [
    path('', movies_list, name='movie'),
    path('<int:pk>/', movies_list_by_id, name='movie_id')
]