from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated


# 📌 Permissões customizadas
class IsAdministradorGeral(permissions.BasePermission):
    """
    Permissão apenas para administradores gerais.
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and hasattr(request.user, 'administradorgeral')


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


class IsMoradorDono(permissions.BasePermission):
    """
    Permissão se o usuário for o morador vinculado ao objeto.
    """
    def has_object_permission(self, request, view, obj):
        return (
            hasattr(obj, 'morador') and 
            obj.morador and 
            hasattr(obj.morador, 'email') and
            obj.morador.email == request.user.email
        )


class IsPortaria(permissions.BasePermission):
    """
    Permissão para usuários da portaria (sem vínculo de morador ou admin).
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and not (
            hasattr(request.user, 'morador') or hasattr(request.user, 'administradorgeral')
        )


class IsPublicReadOnly(permissions.BasePermission):
    """
    Permite leitura (GET), exige login para escrita (POST, PUT, DELETE).
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated


# 📦 Dicionário com permissões por ViewSet
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
    'UnidadeViewSet': [IsAuthenticated, IsPublicReadOnly],  # 👈 Atualizado aqui
    'PrestadorViewSet': [IsAuthenticated],
    'EspacoComumViewSet': [IsAuthenticated],
    'RelatorioViewSet': [IsAuthenticated, IsAdministradorGeral],
}


# 🔧 Função auxiliar para aplicar permissões dinamicamente
def get_viewset_permissions(viewset_name):
    return PERMISSIONS_BY_VIEWSET.get(viewset_name, [IsAuthenticated])
