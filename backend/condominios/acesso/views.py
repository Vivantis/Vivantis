from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from .models import ControleAcesso
from .serializers import ControleAcessoSerializer
from .permissions import get_viewset_permissions

# ─────────────────────────────────────────────────────────────
# 🚪 ViewSet para Controle de Acesso
# ─────────────────────────────────────────────────────────────
class ControleAcessoViewSet(viewsets.ModelViewSet):
    """
    Permite listar, criar e atualizar entradas e saídas de moradores, visitantes e prestadores.
    """
    queryset = ControleAcesso.objects.all().order_by('-data_entrada')
    serializer_class = ControleAcessoSerializer
    permission_classes = get_viewset_permissions('ControleAcessoViewSet')

    # 🔍 Permite filtros via ?tipo=morador&unidade=1
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['tipo', 'morador', 'visitante', 'prestador', 'unidade']
