from rest_framework.permissions import IsAuthenticated, BasePermission

class IsAdministradorGeral(BasePermission):
    """
    Permite acesso apenas a administradores gerais (ex: is_staff).
    """
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.is_staff)

class IsProprietarioOuAdmin(BasePermission):
    """
    Permite acesso apenas ao proprietário do objeto ou a administradores gerais.
    """
    def has_permission(self, request, view):
        # Qualquer usuário autenticado pode listar/criar; o controle fino é feito em has_object_permission
        return bool(request.user and request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        # Admin geral sempre pode
        if request.user.is_staff:
            return True
        # Proprietário: o objeto deve ter atributo `morador.user`
        morador = getattr(obj, 'morador', None)
        return bool(morador and getattr(morador, 'user', None) == request.user)

def get_viewset_permissions(viewset_name):
    """
    Fallback: qualquer ViewSet exige autenticação.
    Modules específicos devem usar seu próprio get_viewset_permissions.
    """
    return [IsAuthenticated]
