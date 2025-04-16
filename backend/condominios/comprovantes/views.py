from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from condominios.models import ComprovantePagamento
from condominios.serializers import ComprovantePagamentoSerializer

class ComprovantePagamentoViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gerenciamento de Comprovantes de Pagamento.
    Permite listar, criar, editar e excluir comprovantes.
    Inclui filtros, busca e ordenação.
    """
    queryset = ComprovantePagamento.objects.all().order_by('-data_envio')
    serializer_class = ComprovantePagamentoSerializer

    # Ativa filtros, ordenação e busca
    filter_backends = [
        DjangoFilterBackend,  # permite filtro direto na URL (ex: ?morador=1)
        filters.OrderingFilter,  # permite ordenação (ex: ?ordering=-data_envio)
        filters.SearchFilter  # permite busca textual (ex: ?search=pagamento)
    ]

    # Campos que podem ser filtrados via query string
    filterset_fields = ['morador', 'cobranca', 'validado']

    # Campos permitidos para ordenação
    ordering_fields = ['data_envio', 'comentario']

    # Campos onde a busca textual será aplicada
    search_fields = ['comentario']
