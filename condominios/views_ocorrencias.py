from rest_framework import viewsets
from .models import Ocorrencia
from .serializers import OcorrenciaSerializer

# ViewSet para o modelo Ocorrencia
# Permite criar, listar, editar e deletar ocorrências via API
class OcorrenciaViewSet(viewsets.ModelViewSet):
    queryset = Ocorrencia.objects.all()
    serializer_class = OcorrenciaSerializer
