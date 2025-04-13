from rest_framework import viewsets
from .models import Ocorrencia
from .serializers import OcorrenciaSerializer
from .permissions import get_viewset_permissions  # 🔐 Importa as permissões dinâmicas

# ─────────────────────────────────────────────────────────────
# 📢 ViewSet para o modelo Ocorrência
# Permite moradores registrarem problemas e administradores acompanharem
# ─────────────────────────────────────────────────────────────
class OcorrenciaViewSet(viewsets.ModelViewSet):
    queryset = Ocorrencia.objects.all()
    serializer_class = OcorrenciaSerializer
    permission_classes = get_viewset_permissions('OcorrenciaViewSet')  # 🔐 Aplica as permissões definidas
