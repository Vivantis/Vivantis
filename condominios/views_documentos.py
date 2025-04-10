from rest_framework import viewsets
from .models import Documento
from .serializers import DocumentoSerializer

# ViewSet para o modelo Documento
# Permite listar, criar, editar e deletar documentos de um condomínio
class DocumentoViewSet(viewsets.ModelViewSet):
    queryset = Documento.objects.all().order_by('-data_envio')  # Lista os mais recentes primeiro
    serializer_class = DocumentoSerializer
