from rest_framework.permissions import IsAuthenticated
from core.permissions import IsAdministradorGeral

def get_viewset_permissions(viewset_name):
    """
    Permissões específicas para o módulo de Documentos.
    - Apenas administradores podem criar, editar ou deletar.
    - Moradores autenticados podem visualizar documentos.
    """
    if viewset_name == 'DocumentoViewSet':
        return [IsAuthenticated, IsAdministradorGeral]
    return [IsAuthenticated]
