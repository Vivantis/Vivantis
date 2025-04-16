from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Prestador
from .serializers import PrestadorSerializer
from .permissions import get_viewset_permissions


# 👷 ViewSet para Prestadores de Serviço
# Permite que administradores registrem e gerenciem prestadores
class PrestadorViewSet(viewsets.ModelViewSet):
    queryset = Prestador.objects.all()
    serializer_class = PrestadorSerializer
    permission_classes = get_viewset_permissions('PrestadorViewSet')

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['tipo_servico', 'condominio']  # 🔍 Exemplo de filtros úteis
    search_fields = ['nome']
    ordering_fields = ['nome']
