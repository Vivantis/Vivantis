from rest_framework import viewsets
from .models import Correspondencia
from .serializers import CorrespondenciaSerializer

# ViewSet para o modelo Correspondência
# Permite listar, criar, editar e deletar registros de entregas
class CorrespondenciaViewSet(viewsets.ModelViewSet):
    queryset = Correspondencia.objects.all().order_by('-data_recebimento')
    serializer_class = CorrespondenciaSerializer
