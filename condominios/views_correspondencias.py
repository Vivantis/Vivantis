# condominios/views_correspondencias.py

from rest_framework import viewsets
from .models import Correspondencia
from .serializers import CorrespondenciaSerializer
from .permissions import get_viewset_permissions  # 🔐 Importa as permissões baseadas em ViewSet

# ViewSet para o modelo Correspondência
# Permite listar, criar, editar e deletar registros de entregas e encomendas
class CorrespondenciaViewSet(viewsets.ModelViewSet):
    queryset = Correspondencia.objects.all().order_by('-data_recebimento')  # Mostra os mais recentes primeiro
    serializer_class = CorrespondenciaSerializer
    permission_classes = get_viewset_permissions('CorrespondenciaViewSet')  # 🔐 Aplica permissões por ViewSet
