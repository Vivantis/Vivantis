from rest_framework import viewsets
from .models import Manutencao
from .serializers import ManutencaoSerializer
from .permissions import get_viewset_permissions  # 🔐 Importa as permissões dinâmicas

# ─────────────────────────────────────────────────────────────
# 🔧 ViewSet para o modelo Manutenção
# Permite listar, criar, editar e deletar manutenções agendadas
# ─────────────────────────────────────────────────────────────
class ManutencaoViewSet(viewsets.ModelViewSet):
    queryset = Manutencao.objects.all().order_by('-data_inicio')  # Ordem decrescente por data
    serializer_class = ManutencaoSerializer
    permission_classes = get_viewset_permissions('ManutencaoViewSet')  # 🔐 Aplica as permissões definidas no dicionário
