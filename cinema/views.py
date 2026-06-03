from rest_framework.generics import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from cinema.serializers import MovieSerializer
from cinema.models import Movie


def cinema_list(request):
    ...

def cinema_detail(request, pk):
    ...
