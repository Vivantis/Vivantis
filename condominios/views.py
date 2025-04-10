from rest_framework import viewsets
from .models import Condominio, Unidade, Morador
from .serializers import CondominioSerializer, UnidadeSerializer, MoradorSerializer

# ViewSet para o modelo Condominio
# Fornece endpoints para listar, criar, editar e deletar condomínios
class CondominioViewSet(viewsets.ModelViewSet):
    queryset = Condominio.objects.all()
    serializer_class = CondominioSerializer

# ViewSet para o modelo Unidade
# Permite visualizar e manipular unidades vinculadas a condomínios
class UnidadeViewSet(viewsets.ModelViewSet):
    queryset = Unidade.objects.all()
    serializer_class = UnidadeSerializer

# ViewSet para o modelo Morador
# Permite gerenciamento dos moradores vinculados às unidades
class MoradorViewSet(viewsets.ModelViewSet):
    queryset = Morador.objects.all()
    serializer_class = MoradorSerializer
