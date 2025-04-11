from rest_framework import generics
from .models import PerfilUsuario
from .serializers import PerfilUsuarioSerializer
from .permissions import get_viewset_permissions  # 🔐 Importa as permissões dinâmicas

# ─────────────────────────────────────────────────────────────
# 👤 View para Perfil do Usuário logado
# Permite ao usuário autenticado visualizar e editar seu próprio perfil
# ─────────────────────────────────────────────────────────────
class MeuPerfilView(generics.RetrieveUpdateAPIView):
    serializer_class = PerfilUsuarioSerializer
    permission_classes = get_viewset_permissions('PerfilUsuarioViewSet')  # 🔐 Aplica permissão

    def get_object(self):
        # Retorna ou cria um perfil vinculado ao usuário autenticado
        return PerfilUsuario.objects.get_or_create(user=self.request.user)[0]
