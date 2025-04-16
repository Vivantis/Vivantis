from rest_framework.permissions import IsAuthenticated, BasePermission


class IsProprietarioOuAdmin(BasePermission):
    """
    Permite acesso se o usuário for administrador geral ou dono do comprovante (morador vinculado).
    """
    def has_object_permission(self, request, view, obj):
        user = request.user
        if not user.is_authenticated:
            return False
        if hasattr(user, 'administradorgeral'):
            return True
        return hasattr(obj, 'morador') and obj.morador and obj.morador.user == user


PERMISSIONS_BY_VIEWSET = {
    'ComprovantePagamentoViewSet': [IsAuthenticated, IsProprietarioOuAdmin],
}


def get_viewset_permissions(viewset_name):
    """
    Função utilitária que retorna as permissões configuradas para o ViewSet.
    """
    return PERMISSIONS_BY_VIEWSET.get(viewset_name, [IsAuthenticated])
