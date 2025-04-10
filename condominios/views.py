from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Condominio, Unidade, Morador
from .serializers import CondominioSerializer, UnidadeSerializer, MoradorSerializer

# ViewSet para o modelo Condominio
# Fornece endpoints para listar, criar, editar e deletar condomínios
class CondominioViewSet(viewsets.ModelViewSet):
    queryset = Condominio.objects.all()
    serializer_class = CondominioSerializer
    # Requer que o usuário esteja autenticado (token JWT)
    permission_classes = [IsAuthenticated]


# ViewSet para o modelo Unidade
# Permite visualizar e manipular unidades vinculadas a um condomínio
class UnidadeViewSet(viewsets.ModelViewSet):
    queryset = Unidade.objects.all()
    serializer_class = UnidadeSerializer
    # Segurança: exige autenticação
    permission_classes = [IsAuthenticated]


# ViewSet para o modelo Morador
# Permite o gerenciamento dos moradores vinculados às unidades
class MoradorViewSet(viewsets.ModelViewSet):
    queryset = Morador.objects.all()
    serializer_class = MoradorSerializer
    # Autenticação obrigatória para acessar os dados dos moradores
    permission_classes = [IsAuthenticated]
