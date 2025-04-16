# condominios/views_cobrancas.py

from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Cobranca
from .serializers import CobrancaSerializer
from .permissions import get_viewset_permissions

# ViewSet para o modelo Cobranca
# Permite criar, listar, editar e deletar cobranças
# Acesso restrito a administradores gerais
class CobrancaViewSet(viewsets.ModelViewSet):
    queryset = Cobranca.objects.all().order_by('-vencimento')  # Mostra as mais recentes primeiro
    serializer_class = CobrancaSerializer
    permission_classes = get_viewset_permissions('CobrancaViewSet')

    # Habilita filtros e ordenação
    filter_backends = [
        DjangoFilterBackend,     # ?status=pago
        filters.OrderingFilter,  # ?ordering=-valor
        filters.SearchFilter     # ?search=descricao
    ]

    # Campos para filtro exato
    filterset_fields = ['status', 'tipo', 'morador', 'unidade', 'vencimento']

    # Campos para ordenação
    ordering_fields = ['valor', 'vencimento', 'status']

    # Campos para busca textual
    search_fields = ['descricao']
