from rest_framework.permissions import BasePermission

class EhAutorOuAdmin(BasePermission):
    """
    Permite acesso apenas se for o criador do relatório ou admin.
    """
    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or obj.gerado_por == request.user
