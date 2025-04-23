from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import Ocorrencia
from .serializers import OcorrenciaSerializer
from .permissions import get_viewset_permissions  # 🔐 Importa o wrapper de permissões

class OcorrenciaViewSet(viewsets.ModelViewSet):
    """
    ViewSet para o modelo Ocorrência.
    Permite moradores registrarem problemas e administradores acompanharem.
    """
    queryset = Ocorrencia.objects.all().order_by('-data_registro')
    serializer_class = OcorrenciaSerializer

    # Habilita filtros por query params
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status', 'morador', 'unidade']

    def get_permissions(self):
        """
        Retorna instâncias das permissões apropriadas para este ViewSet,
        usando o nome da classe para buscar em condominios/ocorrencia/permissions.py.
        """
        permission_classes = get_viewset_permissions(self.__class__.__name__)
        return [permission() for permission in permission_classes]
