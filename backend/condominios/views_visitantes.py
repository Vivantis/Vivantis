from rest_framework import viewsets
from .models import Visitante
from .serializers import VisitanteSerializer
from .permissions import get_viewset_permissions  # 🔐 Importa as permissões baseadas em ViewSet

# ─────────────────────────────────────────────────────────────
# 👥 ViewSet para Visitantes
# ─────────────────────────────────────────────────────────────
class VisitanteViewSet(viewsets.ModelViewSet):
    queryset = Visitante.objects.all()  # Retorna todos os visitantes do banco
    serializer_class = VisitanteSerializer  # Usa o serializer para manipular os dados
    permission_classes = get_viewset_permissions('VisitanteViewSet')  # 🔐 Aplica permissões
