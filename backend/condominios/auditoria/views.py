# condominios/views_auditoria.py

from rest_framework import viewsets
from .models import Auditoria
from .serializers import AuditoriaSerializer
from .permissions import get_viewset_permissions

# ViewSet para leitura do histórico de ações (auditoria)
class AuditoriaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Auditoria.objects.all().order_by('-data')
    serializer_class = AuditoriaSerializer
    permission_classes = get_viewset_permissions('AuditoriaViewSet')
