from rest_framework import viewsets
from .models import EspacoComum, ReservaEspaco
from .serializers import EspacoComumSerializer, ReservaEspacoSerializer
from .permissions import get_viewset_permissions  # 🔐 Importa função de permissões dinâmicas

# ─────────────────────────────────────────────────────────────
# 🧱 ViewSet para Espaços Comuns
# ─────────────────────────────────────────────────────────────
class EspacoComumViewSet(viewsets.ModelViewSet):
    queryset = EspacoComum.objects.all()
    serializer_class = EspacoComumSerializer
    permission_classes = get_viewset_permissions('EspacoComumViewSet')  # 🔐 Aplica permissões


# ─────────────────────────────────────────────────────────────
# 📅 ViewSet para Reservas de Espaços
# ─────────────────────────────────────────────────────────────
class ReservaEspacoViewSet(viewsets.ModelViewSet):
    queryset = ReservaEspaco.objects.all().order_by('-data_reserva', '-horario_inicio')
    serializer_class = ReservaEspacoSerializer
    permission_classes = get_viewset_permissions('ReservaEspacoViewSet')  # 🔐 Aplica permissões
