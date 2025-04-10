from rest_framework import viewsets
from .models import Visitante
from .serializers import VisitanteSerializer

# ViewSet para o modelo Visitante
# Permite operações de listagem, criação, edição e exclusão via API
class VisitanteViewSet(viewsets.ModelViewSet):
    queryset = Visitante.objects.all()  # Retorna todos os visitantes do banco
    serializer_class = VisitanteSerializer  # Usa o serializer para manipular os dados
