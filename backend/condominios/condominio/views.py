from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend

from condominios.condominio.models import Condominio
from condominios.condominio.serializers import CondominioSerializer
from core.permissions import get_viewset_permissions


# ─────────────────────────────────────────────────────────────
# 🏢 ViewSet para o modelo Condominio
# ─────────────────────────────────────────────────────────────
class CondominioViewSet(viewsets.ModelViewSet):
    queryset = Condominio.objects.all().order_by('nome')
    serializer_class = CondominioSerializer
    permission_classes = get_viewset_permissions('CondominioViewSet')

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['cidade', 'estado', 'ativo']
    search_fields = ['nome', 'endereco']
    ordering_fields = ['nome', 'cidade']
    ordering = ['nome']
