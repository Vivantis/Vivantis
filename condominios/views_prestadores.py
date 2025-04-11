# condominios/views_prestadores.py

from rest_framework import viewsets
from .models import Prestador
from .serializers import PrestadorSerializer
from .permissions import get_viewset_permissions  # 🔐 Importa as permissões por ViewSet

# ─────────────────────────────────────────────────────────────
# 🛠️ ViewSet para Prestadores de Serviço
# Fornece os endpoints da API para listar, criar, editar e excluir prestadores vinculados ao condomínio
# ─────────────────────────────────────────────────────────────
class PrestadorViewSet(viewsets.ModelViewSet):
    queryset = Prestador.objects.all()
    serializer_class = PrestadorSerializer
    permission_classes = get_viewset_permissions('PrestadorViewSet')  # 🔐 Permissões aplicadas dinamicamente
