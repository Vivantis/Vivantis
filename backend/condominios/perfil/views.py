from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import PerfilUsuario
from .serializers import PerfilUsuarioSerializer

class PerfilUsuarioViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gerenciamento do perfil do usuário.
    """
    queryset = PerfilUsuario.objects.all()
    serializer_class = PerfilUsuarioSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        # Usuário staff vê todos; caso contrário, só seu próprio perfil
        if user.is_staff:
            return PerfilUsuario.objects.all()
        return PerfilUsuario.objects.filter(user=user)
