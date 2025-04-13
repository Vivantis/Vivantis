
from rest_framework import permissions


class IsAdministradorGeral(permissions.BasePermission):
    """
    Permissão apenas para administradores gerais.
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and hasattr(request.user, 'administradorgeral')


class IsMoradorDono(permissions.BasePermission):
    """
    Permite acesso se o morador autenticado for dono do objeto.
    Requer que o objeto tenha um campo "morador".
    """
    def has_object_permission(self, request, view, obj):
        return (
            hasattr(obj, 'morador') and 
            obj.morador and 
            hasattr(obj.morador, 'email') and
            obj.morador.email == request.user.email
        )


class IsProprietarioOuAdmin(permissions.BasePermission):
    """
    Permissão para donos dos dados ou administradores gerais.
    """
    def has_object_permission(self, request, view, obj):
        if request.user and request.user.is_authenticated:
            if hasattr(request.user, 'administradorgeral'):
                return True
            if (
                hasattr(obj, 'morador') and 
                obj.morador and 
                hasattr(obj.morador, 'email') and 
                obj.morador.email == request.user.email
            ):
                return True
        return False


class IsPortaria(permissions.BasePermission):
    """
    Permissão básica para usuários da portaria (usuários sem perfil de morador ou admin).
    Pode ser adaptada caso precise ser mais específica.
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and not (
            hasattr(request.user, 'morador') or hasattr(request.user, 'administradorgeral')
        )


class IsPublicReadOnly(permissions.BasePermission):
    """
    Permissão que permite leitura pública (GET), mas exige login para ações de escrita.
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated


from rest_framework.permissions import IsAuthenticated

PERMISSIONS_BY_VIEWSET = {
    'DocumentoViewSet': [IsAuthenticated, IsAdministradorGeral],
    'CobrancaViewSet': [IsAuthenticated, IsAdministradorGeral],
    'ComprovantePagamentoViewSet': [IsAuthenticated, IsProprietarioOuAdmin],
    'AutorizacaoEntradaViewSet': [IsAuthenticated, IsPortaria],
    'OcorrenciaViewSet': [IsAuthenticated, IsProprietarioOuAdmin],
    'AuditoriaViewSet': [IsAuthenticated, IsAdministradorGeral],
    'AvisoViewSet': [IsAuthenticated, IsAdministradorGeral],
    'ManutencaoViewSet': [IsAuthenticated, IsAdministradorGeral],
    'PerfilUsuarioViewSet': [IsAuthenticated],
    'MoradorViewSet': [IsAuthenticated, IsAdministradorGeral],
    'AdministradorGeralViewSet': [IsAuthenticated, IsAdministradorGeral],
    'ReservaEspacoViewSet': [IsAuthenticated, IsMoradorDono],
    'VisitanteViewSet': [IsAuthenticated],
    'ControleAcessoViewSet': [IsAuthenticated],
    'CorrespondenciaViewSet': [IsAuthenticated],
    'CondominioViewSet': [IsAuthenticated],
    'UnidadeViewSet': [IsAuthenticated],
    'PrestadorViewSet': [IsAuthenticated],
    'EspacoComumViewSet': [IsAuthenticated],
    'RelatorioViewSet': [IsAuthenticated, IsAdministradorGeral],
}


def get_viewset_permissions(viewset_name):
    """
    Função utilitária para aplicar permissões dinamicamente nos ViewSets
    """
    return PERMISSIONS_BY_VIEWSET.get(viewset_name, [IsAuthenticated])
