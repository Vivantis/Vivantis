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