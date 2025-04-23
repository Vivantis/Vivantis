from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Prestador
from .serializer import PrestadorSerializer

class PrestadorViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gerenciamento dos prestadores de serviço.
    """
    queryset = Prestador.objects.all()
    serializer_class = PrestadorSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Prestador.objects.all()
        return Prestador.objects.filter(condominio__morador__user=user).distinct()
