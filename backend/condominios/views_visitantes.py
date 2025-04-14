from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import Visitante
from .serializers import VisitanteSerializer
from .permissions import get_viewset_permissions  # 🔐 Importa as permissões baseadas em ViewSet

# ─────────────────────────────────────────────────────────────
# 👥 ViewSet para Visitantes
# ─────────────────────────────────────────────────────────────
class VisitanteViewSet(viewsets.ModelViewSet):
    queryset = Visitante.objects.all()
    serializer_class = VisitanteSerializer
    permission_classes = get_viewset_permissions('VisitanteViewSet')

    # 🎯 Filtros habilitados via query params
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['nome', 'documento', 'unidade', 'morador_responsavel']
