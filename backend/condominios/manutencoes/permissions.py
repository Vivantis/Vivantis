from rest_framework.permissions import IsAuthenticated
from condominios.permissions import IsAdministradorGeral

def get_viewset_permissions(viewset_name):
    """
    Aplica permissões específicas para o módulo de Manutenção.
    Apenas administradores gerais podem acessar.
    """
    if viewset_name == 'ManutencaoViewSet':
        return [IsAuthenticated, IsAdministradorGeral]

    # Permissão padrão caso o ViewSet não seja reconhecido
    return [IsAuthenticated]
