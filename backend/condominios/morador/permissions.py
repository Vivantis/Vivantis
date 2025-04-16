class IsMoradorDono(permissions.BasePermission):
    """
    Permite acesso se o morador autenticado for dono do objeto.
    Requer que o objeto tenha um campo 'morador' com um e-mail associado.
    """
    def has_object_permission(self, request, view, obj):
        morador = getattr(obj, 'morador', None)
        if not morador or not hasattr(morador, 'email'):
            return False
        return morador.email == getattr(request.user, 'email', None)
