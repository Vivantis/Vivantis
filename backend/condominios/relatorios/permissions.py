from rest_framework.permissions import IsAuthenticated
from core.permissions import IsAdministradorGeral

def get_viewset_permissions(viewset_name):
    if viewset_name == 'RelatorioViewSet':
        return [IsAuthenticated, IsAdministradorGeral]
    return [IsAuthenticated]
