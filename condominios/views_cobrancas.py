from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Cobranca
from .serializers import CobrancaSerializer

# ViewSet para o modelo Cobranca
# Permite criar, listar, editar e deletar cobranças
class CobrancaViewSet(viewsets.ModelViewSet):
    queryset = Cobranca.objects.all()
    serializer_class = CobrancaSerializer
    permission_classes = [IsAuthenticated]
