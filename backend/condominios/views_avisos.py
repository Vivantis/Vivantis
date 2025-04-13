# condominios/views_avisos.py

from rest_framework import viewsets
from .models import Aviso
from .serializers import AvisoSerializer
from .permissions import get_viewset_permissions  # 🔐 Importa a função de permissões dinâmicas

# ViewSet para o modelo Aviso
# Permite listar, criar, editar e deletar avisos e comunicados do condomínio
class AvisoViewSet(viewsets.ModelViewSet):
    queryset = Aviso.objects.all().order_by('-criado_em')  # Exibe os mais recentes primeiro
    serializer_class = AvisoSerializer
    permission_classes = get_viewset_permissions('AvisoViewSet')  # 🔐 Proteção baseada em perfil
