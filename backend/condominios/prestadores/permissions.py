from rest_framework import permissions

class IsAuthenticated(permissions.IsAuthenticated):
    """
    Apenas usuários autenticados podem acessar o módulo de Prestadores.
    """
    pass


PERMISSIONS_BY_VIEWSET = {
    'PrestadorViewSet': [IsAuthenticated],
}


def get_viewset_permissions(viewset_name):
    """
    Função utilitária para aplicar permissões do módulo Prestadores.
    """
    return PERMISSIONS_BY_VIEWSET.get(viewset_name, [IsAuthenticated])
