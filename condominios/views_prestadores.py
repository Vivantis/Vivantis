# condominios/views_prestadores.py

from rest_framework import viewsets
from .models import Prestador
from .serializers import PrestadorSerializer

# ViewSet para o modelo Prestador
# Fornece os endpoints para listar, criar, editar e deletar prestadores
class PrestadorViewSet(viewsets.ModelViewSet):
    queryset = Prestador.objects.all()
    serializer_class = PrestadorSerializer
