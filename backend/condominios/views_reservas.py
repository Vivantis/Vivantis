# condominios/views_reservas.py

from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import EspacoComum, ReservaEspaco
from .serializers import EspacoComumSerializer, ReservaEspacoSerializer
from .permissions import get_viewset_permissions

# ─────────────────────────────────────────────────────────────
# 📍 ViewSet para Espaços Comuns
# Permite que administradores gerenciem os espaços do condomínio
# ─────────────────────────────────────────────────────────────
class EspacoComumViewSet(viewsets.ModelViewSet):
    queryset = EspacoComum.objects.all().order_by('nome')
    serializer_class = EspacoComumSerializer
    permission_classes = get_viewset_permissions('EspacoComumViewSet')

    # Habilita filtros e busca por query params
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['condominio']         # Ex: ?condominio=1
    search_fields = ['nome']                  # Ex: ?search=salao


# ─────────────────────────────────────────────────────────────
# 📅 ViewSet para Reservas de Espaços
# Permite que moradores reservem espaços e visualizem suas reservas
# ─────────────────────────────────────────────────────────────
class ReservaEspacoViewSet(viewsets.ModelViewSet):
    queryset = ReservaEspaco.objects.all().order_by('-data_reserva')
    serializer_class = ReservaEspacoSerializer
    permission_classes = get_viewset_permissions('ReservaEspacoViewSet')

    # Habilita filtros, ordenação e busca
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = [
        'morador',         # Ex: ?morador=1
        'unidade',         # Ex: ?unidade=2
        'espaco',          # Ex: ?espaco=5
        'data_reserva',    # Ex: ?data_reserva=2025-04-20
        'status'           # Ex: ?status=pendente
    ]
    ordering_fields = ['data_reserva', 'horario_inicio']   # Ex: ?ordering=data_reserva
    search_fields = ['observacoes']                        # Ex: ?search=aniversario
