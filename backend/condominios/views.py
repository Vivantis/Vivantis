from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from .models import Condominio, Unidade, Morador
from .serializers import CondominioSerializer, UnidadeSerializer, MoradorSerializer


# ViewSet para o modelo Condominio
class CondominioViewSet(viewsets.ModelViewSet):
    queryset = Condominio.objects.all()
    serializer_class = CondominioSerializer
    permission_classes = [IsAuthenticated]


# ViewSet para o modelo Unidade
class UnidadeViewSet(viewsets.ModelViewSet):
    queryset = Unidade.objects.all()
    serializer_class = UnidadeSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['numero', 'bloco', 'condominio']


# ViewSet para o modelo Morador
class MoradorViewSet(viewsets.ModelViewSet):
    queryset = Morador.objects.all()
    serializer_class = MoradorSerializer
    permission_classes = [IsAuthenticated]

    # Agora permite tanto filtro exato (email, unidade) quanto busca parcial (nome)
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['email', 'unidade']  # busca exata
    search_fields = ['nome']  # busca parcial com ?search=Maria
