from rest_framework import permissions


class IsPortaria(permissions.BasePermission):
    """
    Permissão para usuários da portaria.
    Somente eles podem criar autorizações.
    """
    def has_permission(self, request, view):
        return (
            request.user and request.user.is_authenticated and
            not hasattr(request.user, 'morador') and
            not hasattr(request.user, 'administradorgeral')
        )


class IsMoradorResponsavel(permissions.BasePermission):
    """
    Permissão para que apenas o morador responsável possa responder a solicitação.
    """
    def has_object_permission(self, request, view, obj):
        return (
            request.user and request.user.is_authenticated and
            hasattr(request.user, 'morador') and
            obj.unidade_destino == request.user.morador.unidade
        )


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Permite leitura para todos autenticados, mas só administradores gerais podem alterar.
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return request.user and request.user.is_authenticated
        return request.user and hasattr(request.user, 'administradorgeral')


# Dicionário de permissões por ViewSet
from rest_framework.permissions import IsAuthenticated

PERMISSIONS_BY_VIEWSET = {
    'AutorizacaoEntradaViewSet': [IsAuthenticated, IsPortaria],
}

def get_viewset_permissions(viewset_name):
    return PERMISSIONS_BY_VIEWSET.get(viewset_name, [IsAuthenticated])
