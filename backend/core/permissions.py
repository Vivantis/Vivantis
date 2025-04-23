from rest_framework.permissions import IsAuthenticated, BasePermission

class IsAdministradorGeral(BasePermission):
    """
    Permite acesso apenas a administradores gerais (ex: is_staff).
    """
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.is_staff)

def get_viewset_permissions(viewset_name):
    # Por enquanto, tudo exige autenticação
    return [IsAuthenticated]
