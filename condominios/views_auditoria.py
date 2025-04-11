from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Auditoria
from .serializers import AuditoriaSerializer

# ViewSet para leitura do histórico de ações (auditoria)
class AuditoriaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Auditoria.objects.all().order_by('-data')
    serializer_class = AuditoriaSerializer
    permission_classes = [IsAuthenticated]
