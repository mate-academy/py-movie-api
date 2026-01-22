from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import Movie
from .serializers import MovieSerializer

class MovieViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite visualizar ou editar filmes.
    GET /movies/ -> Lista todos
    GET /movies/<pk>/ -> Detalhe
    POST /movies/ -> Cria
    PUT /movies/<pk>/ -> Atualiza (completo)
    DELETE /movies/<pk>/ -> Deleta
    """
    queryset = Movie.objects.all().order_by("id")
    serializer_class = MovieSerializer
    # Permissão: AllowAny para fins de teste, conforme o padrão de APIs simples
    permission_classes = [AllowAny]
