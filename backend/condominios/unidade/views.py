# condominios/unidade/views.py

from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from condominios.unidade.models import Unidade
from condominios.unidade.serializers import UnidadeSerializer
from core.permissions import get_viewset_permissions


# ─────────────────────────────────────────────────────────────
# 🏠 ViewSet para o modelo Unidade
# ─────────────────────────────────────────────────────────────
class UnidadeViewSet(viewsets.ModelViewSet):
    queryset = Unidade.objects.all()
    serializer_class = UnidadeSerializer
    permission_classes = get_viewset_permissions('UnidadeViewSet')

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['numero', 'bloco', 'condominio']
    search_fields = ['numero', 'bloco']
    ordering_fields = ['numero', 'bloco']
    ordering = ['numero']
