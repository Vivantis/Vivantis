from rest_framework import viewsets, filters, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from .models import Condominio, Unidade, Morador
from .serializers import CondominioSerializer, UnidadeSerializer, MoradorSerializer
from .permissions import get_viewset_permissions  # Certifique-se de importar isso

# ─────────────────────────────────────────────────────────────
# 🏢 ViewSet para o modelo Condominio
# ─────────────────────────────────────────────────────────────
class CondominioViewSet(viewsets.ModelViewSet):
    queryset = Condominio.objects.all().order_by('nome')
    serializer_class = CondominioSerializer
    permission_classes = get_viewset_permissions('CondominioViewSet')

    # Habilita filtros, busca e ordenação
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['cidade', 'estado', 'ativo']     # Ex: ?cidade=Curitiba&ativo=True
    search_fields = ['nome', 'endereco']                 # Ex: ?search=Edifício Central
    ordering_fields = ['nome', 'cidade']                 # Ex: ?ordering=nome

# ─────────────────────────────────────────────────────────────
# 🏠 ViewSet para o modelo Unidade
# ─────────────────────────────────────────────────────────────
class UnidadeViewSet(viewsets.ModelViewSet):
    queryset = Unidade.objects.all()
    serializer_class = UnidadeSerializer
    permission_classes = get_viewset_permissions('UnidadeViewSet')
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['numero', 'bloco', 'condominio']

# ─────────────────────────────────────────────────────────────
# 👤 ViewSet para o modelo Morador
# ─────────────────────────────────────────────────────────────
class MoradorViewSet(viewsets.ModelViewSet):
    queryset = Morador.objects.all()
    serializer_class = MoradorSerializer
    permission_classes = get_viewset_permissions('MoradorViewSet')
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['email', 'unidade']
    search_fields = ['nome']

    # 🔒 Endpoint: POST /api/moradores/{id}/aprovar/
    @action(detail=True, methods=['post'], url_path='aprovar')
    def aprovar_morador(self, request, pk=None):
        """
        Ativa o usuário vinculado ao morador (campo .user)
        Requer autenticação com permissão de AdministradorGeral.
        """
        morador = self.get_object()
        if morador.user:
            morador.user.is_active = True
            morador.user.save()
            return Response({'status': 'Morador aprovado com sucesso'}, status=status.HTTP_200_OK)
        return Response({'error': 'Morador não possui usuário vinculado'}, status=status.HTTP_400_BAD_REQUEST)
