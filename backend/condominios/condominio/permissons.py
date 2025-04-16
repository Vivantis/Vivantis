from rest_framework import permissions


class IsAdministradorGeral(permissions.BasePermission):
    """
    Permissão exclusiva para administradores gerais.
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and hasattr(request.user, 'administradorgeral')


class IsPublicReadOnly(permissions.BasePermission):
    """
    Permite leitura pública (GET), exige autenticação para qualquer outra ação.
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated


# Dicionário com mapeamento de permissões por ViewSet
from rest_framework.permissions import IsAuthenticated

PERMISSIONS_BY_VIEWSET = {
    'CondominioViewSet': [IsAuthenticated, IsAdministradorGeral],
    'UnidadeViewSet': [IsAuthenticated],
}

def get_viewset_permissions(viewset_name):
    """
    Função auxiliar para recuperar as permissões de acordo com o nome da ViewSet.
    """
    return PERMISSIONS_BY_VIEWSET.get(viewset_name, [IsAuthenticated])
