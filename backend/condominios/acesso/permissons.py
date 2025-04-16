from rest_framework import permissions

class IsAutenticado(permissions.BasePermission):
    """
    Permite acesso apenas a usuários autenticados.
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated
