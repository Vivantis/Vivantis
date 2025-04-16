from rest_framework.permissions import IsAuthenticated
from condominios.permissions import IsProprietarioOuAdmin

PERMISSIONS_BY_VIEWSET = {
    'OcorrenciaViewSet': [IsAuthenticated, IsProprietarioOuAdmin],
}


def get_viewset_permissions(viewset_name):
    """
    Retorna as permissões específicas para os ViewSets do módulo de Ocorrências.
    """
    return PERMISSIONS_BY_VIEWSET.get(viewset_name, [IsAuthenticated])
