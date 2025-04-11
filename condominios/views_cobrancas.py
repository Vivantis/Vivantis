# condominios/views_cobrancas.py

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Cobranca
from .serializers import CobrancaSerializer
from .permissions import get_viewset_permissions

# ViewSet para o modelo Cobranca
# Permite criar, listar, editar e deletar cobranças
# Acesso restrito a administradores gerais
class CobrancaViewSet(viewsets.ModelViewSet):
    queryset = Cobranca.objects.all()
    serializer_class = CobrancaSerializer
    permission_classes = get_viewset_permissions('CobrancaViewSet')
