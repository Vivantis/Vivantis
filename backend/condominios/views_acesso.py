from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import ControleAcesso
from .serializers import ControleAcessoSerializer
from .permissions import get_viewset_permissions

# ViewSet para o modelo Controle de Acesso
# Permite registrar entradas e saídas via API
class ControleAcessoViewSet(viewsets.ModelViewSet):
    queryset = ControleAcesso.objects.all().order_by('-data_entrada')
    serializer_class = ControleAcessoSerializer
    permission_classes = get_viewset_permissions('ControleAcessoViewSet')

    # Filtros via query params (tipo, morador, visitante, prestador, unidade)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['tipo', 'morador', 'visitante', 'prestador', 'unidade']
