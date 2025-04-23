from rest_framework.permissions import IsAuthenticated
from core.permissions import IsProprietarioOuAdmin

def get_viewset_permissions(viewset_name):
    """
    Permissões para o módulo de Ocorrências:
    - Moradores autenticados podem listar e criar suas ocorrências.
    - Proprietário ou administrador geral pode ver/editar/todos.
    """
    if viewset_name == 'OcorrenciaViewSet':
        return [IsAuthenticated, IsProprietarioOuAdmin]
    return [IsAuthenticated]
