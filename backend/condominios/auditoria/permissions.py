# backend/condominios/auditoria/permissions.py

from rest_framework.permissions import IsAuthenticated
from core.permissions import IsAdministradorGeral

def get_viewset_permissions(viewset_name):
    """
    Permissões para o módulo de Auditoria:
    - Usuários autenticados podem listar suas próprias ações de auditoria.
    - Administradores gerais podem ver tudo.
    """
    if viewset_name == 'AuditoriaViewSet':
        return [IsAuthenticated, IsAdministradorGeral]
    return [IsAuthenticated]
