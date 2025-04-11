from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Documento
from .serializers import DocumentoSerializer
from .permissions import get_viewset_permissions  # ⬅️ Importa a função que define as permissões por ViewSet

# ViewSet para o modelo Documento
# Permite listar, criar, editar e deletar documentos de um condomínio
class DocumentoViewSet(viewsets.ModelViewSet):
    queryset = Documento.objects.all().order_by('-data_envio')  # Lista os mais recentes primeiro
    serializer_class = DocumentoSerializer
    permission_classes = get_viewset_permissions('DocumentoViewSet')  # ⬅️ Aplica as permissões específicas
