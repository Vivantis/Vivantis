from rest_framework.permissions import BasePermission

class EhMoradorDoCondominioOuAdmin(BasePermission):
    """
    Permite acesso se o usuário for admin ou morador do condomínio vinculado ao prestador.
    """
    def has_object_permission(self, request, view, obj):
        user = request.user
        if user.is_staff:
            return True
        return hasattr(user, 'morador') and obj.condominio == user.morador.unidade.condominio
