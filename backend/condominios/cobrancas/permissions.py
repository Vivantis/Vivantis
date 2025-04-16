from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated

# ─────────────────────────────────────────────────────────────
# Permissões customizadas reutilizáveis
# ─────────────────────────────────────────────────────────────

class IsAdministradorGeral(permissions.BasePermission):
    """
    Permissão apenas para administradores gerais.
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and hasattr(request.user, 'administradorgeral')


class IsProprietarioOuAdmin(permissions.BasePermission):
    """
    Permissão para donos dos dados (morador) ou administradores gerais.
    """
    def has_object_permission(self, request, view, obj):
        if request.user and request.user.is_authenticated:
            if hasattr(request.user, 'administradorgeral'):
                return True
            if (
                hasattr(obj, 'morador') and 
                obj.morador and 
                hasattr(obj.morador, 'email') and 
                obj.morador.email == request.user.email
            ):
                return True
        return False

# (Outras permissões como IsPortaria, IsPublicReadOnly podem ficar aqui se forem usadas por outros módulos)


# ─────────────────────────────────────────────────────────────
# Permissões por ViewSet
# ─────────────────────────────────────────────────────────────

PERMISSIONS_BY_VIEWSET = {
    'CobrancaViewSet': [IsAuthenticated, IsAdministradorGeral],  # Somente administradores podem gerenciar
    # Outras permissões podem ser adicionadas aqui, se necessário
}


def get_viewset_permissions(viewset_name):
    """
    Função utilitária para aplicar permissões dinamicamente nos ViewSets.
    """
    return PERMISSIONS_BY_VIEWSET.get(viewset_name, [IsAuthenticated])
