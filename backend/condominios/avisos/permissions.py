from rest_framework.permissions import IsAuthenticated
from condominios.permissions import IsAdministradorGeral

PERMISSIONS_BY_VIEWSET = {
    'AvisoViewSet': [IsAuthenticated, IsAdministradorGeral],
}
