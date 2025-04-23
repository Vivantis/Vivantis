from rest_framework.permissions import IsAuthenticated
from core.permissions import IsProprietarioOuAdmin, IsAdministradorGeral

def get_viewset_permissions(viewset_name):
    """
    Permissões para o módulo de Correspondência:
    - Usuários autenticados podem listar e criar suas próprias correspondências.
    - Proprietário ou administrador geral pode editar/excluir qualquer.
    """
    if viewset_name == 'CorrespondenciaViewSet':
        return [IsAuthenticated, IsProprietarioOuAdmin]
    return [IsAuthenticated]
