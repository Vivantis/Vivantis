from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import PerfilUsuario
from .serializer import PerfilUsuarioSerializer

class PerfilUsuarioViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gerenciamento do perfil do usuário logado.
    Usuário comum só vê e edita o próprio perfil.
    Admins podem ver todos os perfis.
    """
    queryset = PerfilUsuario.objects.all()
    serializer_class = PerfilUsuarioSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return PerfilUsuario.objects.all()
        return PerfilUsuario.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
