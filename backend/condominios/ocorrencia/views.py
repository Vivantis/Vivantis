from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import Ocorrencia
from .serializers import OcorrenciaSerializer
from .permissions import get_viewset_permissions  # 🔐 Importa as permissões dinâmicas

# ─────────────────────────────────────────────────────────────
# 📢 ViewSet para o modelo Ocorrência
# Permite moradores registrarem problemas e administradores acompanharem
# ─────────────────────────────────────────────────────────────
class OcorrenciaViewSet(viewsets.ModelViewSet):
    queryset = Ocorrencia.objects.all().order_by('-data_registro')
    serializer_class = OcorrenciaSerializer
    permission_classes = get_viewset_permissions('OcorrenciaViewSet')

    # Habilita filtros por query params
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status', 'morador', 'unidade']
