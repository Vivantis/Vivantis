from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Relatorio
from .serializer import RelatorioSerializer

class RelatorioViewSet(viewsets.ModelViewSet):
    """
    ViewSet para listar e registrar relatórios gerados pelo sistema.
    """
    queryset = Relatorio.objects.all().order_by('-data_geracao')
    serializer_class = RelatorioSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(gerado_por=self.request.user)

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Relatorio.objects.all()
        return Relatorio.objects.filter(gerado_por=user)
