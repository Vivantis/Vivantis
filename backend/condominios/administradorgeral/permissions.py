from rest_framework.permissions import IsAuthenticated
from condominios.permissions_base import IsAdministradorGeral  # ou ajuste o import se necessário

PERMISSIONS_BY_VIEWSET = {
    'AdministradorGeralViewSet': [IsAuthenticated, IsAdministradorGeral],
}
