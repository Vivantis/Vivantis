from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from condominios.models import Unidade
from condominios.serializers import UnidadeSerializer
from condominios.permissions import get_viewset_permissions

# ─────────────────────────────────────────────────────────────
# 🏠 ViewSet para o modelo Unidade
# ─────────────────────────────────────────────────────────────
class UnidadeViewSet(viewsets.ModelViewSet):
    queryset = Unidade.objects.all()
    serializer_class = UnidadeSerializer
    permission_classes = get_viewset_permissions('UnidadeViewSet')
    
    # 🔍 Permite filtragem por número, bloco e condomínio via query params
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['numero', 'bloco', 'condominio']
