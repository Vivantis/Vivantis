from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import ComprovantePagamento
from .serializers import ComprovantePagamentoSerializer
from .permissions import get_viewset_permissions

class ComprovantePagamentoViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gerenciamento de Comprovantes de Pagamento.
    Permite listar, criar, editar e excluir comprovantes.
    Inclui filtros, busca e ordenação.
    """
    queryset = ComprovantePagamento.objects.all().order_by('-data_envio')
    serializer_class = ComprovantePagamentoSerializer
    permission_classes = get_viewset_permissions('ComprovantePagamentoViewSet')

    # Ativa filtros, ordenação e busca
    filter_backends = [
        DjangoFilterBackend,    # ?morador=1, ?cobranca=2…
        filters.OrderingFilter, # ?ordering=-data_envio
        filters.SearchFilter    # ?search=pagamento
    ]

    # Campos que podem ser filtrados
    filterset_fields = ['morador', 'cobranca', 'validado']

    # Campos permitidos para ordenação
    ordering_fields = ['data_envio', 'comentario']

    # Campos onde a busca textual será aplicada
    search_fields = ['comentario']
