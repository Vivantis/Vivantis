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

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['cidade', 'estado', 'ativo']
    search_fields = ['nome', 'endereco']
    ordering_fields = ['nome', 'cidade']

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

    # ✅ POST /api/moradores/{id}/aprovar/
    @action(detail=True, methods=['post'], url_path='aprovar')
    def aprovar_morador(self, request, pk=None):
        morador = self.get_object()
        if morador.user:
            morador.user.is_active = True
            morador.user.save()
            return Response({'status': 'Morador aprovado com sucesso'}, status=status.HTTP_200_OK)
        return Response({'error': 'Morador não possui usuário vinculado'}, status=status.HTTP_400_BAD_REQUEST)

    # ✅ PATCH /api/moradores/{id}/delegar-voto/
    @action(detail=True, methods=['patch'], url_path='delegar-voto')
    def delegar_voto(self, request, pk=None):
        """
        Permite que um admin/síndico altere o campo pode_votar de um morador.
        Body esperado: { "pode_votar": true/false }
        """
        morador = self.get_object()
        if 'pode_votar' not in request.data:
            return Response({'error': 'Campo "pode_votar" é obrigatório.'}, status=status.HTTP_400_BAD_REQUEST)

        pode_votar = request.data['pode_votar']
        if not isinstance(pode_votar, bool):
            return Response({'error': '"pode_votar" deve ser true ou false.'}, status=status.HTTP_400_BAD_REQUEST)

        morador.pode_votar = pode_votar
        morador.save()
        return Response({
            'status': 'Atualização de voto realizada com sucesso',
            'morador': morador.nome,
            'pode_votar': morador.pode_votar
        }, status=status.HTTP_200_OK)
