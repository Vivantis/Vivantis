from rest_framework import permissions

class IsMoradorDono(permissions.BasePermission):
    """
    Permite acesso apenas se o morador for o dono da reserva.
    Considera o campo `morador` no objeto.
    """
    def has_object_permission(self, request, view, obj):
        if request.user and request.user.is_authenticated:
            if hasattr(request.user, 'administradorgeral'):
                return True
            if hasattr(obj, 'morador') and obj.morador and obj.morador.email == request.user.email:
                return True
        return False


from rest_framework.permissions import IsAuthenticated

PERMISSIONS_BY_VIEWSET = {
    'ReservaEspacoViewSet': [IsAuthenticated, IsMoradorDono],
    'EspacoComumViewSet': [IsAuthenticated],  # Pode ajustar conforme regras específicas
}


def get_viewset_permissions(viewset_name):
    """
    Aplica as permissões específicas de cada ViewSet no módulo de reservas.
    """
    return PERMISSIONS_BY_VIEWSET.get(viewset_name, [IsAuthenticated])
