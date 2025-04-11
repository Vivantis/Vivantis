from rest_framework import generics, permissions
from .models import PerfilUsuario
from .serializers import PerfilUsuarioSerializer

# 🔐 View que permite ao usuário autenticado visualizar e editar seu perfil
class MeuPerfilView(generics.RetrieveUpdateAPIView):
    serializer_class = PerfilUsuarioSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        # Busca o perfil relacionado ao usuário logado
        return PerfilUsuario.objects.get_or_create(user=self.request.user)[0]
