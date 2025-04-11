# condominios/views_comprovantes.py

from rest_framework import viewsets
from .models import ComprovantePagamento
from .serializers import ComprovantePagamentoSerializer
from .permissions import get_viewset_permissions

# ViewSet para Comprovantes de Pagamento
# Permite enviar, listar e validar comprovantes
# Apenas moradores donos ou administradores têm acesso ao seu conteúdo
class ComprovantePagamentoViewSet(viewsets.ModelViewSet):
    queryset = ComprovantePagamento.objects.all()
    serializer_class = ComprovantePagamentoSerializer
    permission_classes = get_viewset_permissions('ComprovantePagamentoViewSet')
