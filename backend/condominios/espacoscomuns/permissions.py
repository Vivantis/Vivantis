from rest_framework.permissions import IsAuthenticated
from condominios.permissions import IsAdministradorGeral  # já temos essa classe no projeto

PERMISSIONS_BY_VIEWSET = {
    'EspacoComumViewSet': [IsAuthenticated, IsAdministradorGeral],
}

def get_viewset_permissions(viewset_name):
    return PERMISSIONS_BY_VIEWSET.get(viewset_name, [IsAuthenticated])
