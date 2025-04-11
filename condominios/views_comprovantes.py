from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import ComprovantePagamento
from .serializers import ComprovantePagamentoSerializer

# ViewSet para Comprovantes de Pagamento
# Permite enviar, listar e validar comprovantes
class ComprovantePagamentoViewSet(viewsets.ModelViewSet):
    queryset = ComprovantePagamento.objects.all()
    serializer_class = ComprovantePagamentoSerializer
    permission_classes = [IsAuthenticated]
