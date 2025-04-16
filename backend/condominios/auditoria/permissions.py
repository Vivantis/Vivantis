from rest_framework.permissions import IsAuthenticated
from condominios.permissions import IsAdministradorGeral  # já existente no projeto

# Apenas administradores gerais podem acessar auditorias
PERMISSIONS_BY_VIEWSET = {
    'AuditoriaViewSet': [IsAuthenticated, IsAdministradorGeral],
}

def get_viewset_permissions(viewset_name):
    return PERMISSIONS_BY_VIEWSET.get(viewset_name, [IsAuthenticated])
