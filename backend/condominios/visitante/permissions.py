# condominios/visitantes/permissions.py

from rest_framework.permissions import IsAuthenticated

PERMISSIONS_BY_VIEWSET = {
    'VisitanteViewSet': [IsAuthenticated]
}

def get_viewset_permissions(viewset_name):
    return PERMISSIONS_BY_VIEWSET.get(viewset_name, [IsAuthenticated])
