from rest_framework.permissions import IsAuthenticated
from core.permissions import IsProprietarioOuAdmin, IsAdministradorGeral

def get_viewset_permissions(viewset_name):
    """
    Permissões para o módulo de Controle de Acesso:
    - Usuários autenticados podem listar suas entradas/saídas.
    - Proprietário, administrador geral ou staff podem criar/editar/excluir.
    """
    if viewset_name == 'ControleAcessoViewSet':
        # todos autenticados veem; só dono ou admin geram/alteram
        return [IsAuthenticated, IsProprietarioOuAdmin, IsAdministradorGeral]
    return [IsAuthenticated]
