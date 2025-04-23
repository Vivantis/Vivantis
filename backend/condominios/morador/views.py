from rest_framework import viewsets, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from condominios.morador.models import Morador
from condominios.morador.serializers import MoradorSerializer
from core.permissions import get_viewset_permissions


# ─────────────────────────────────────────────────────────────
# 👤 ViewSet para o modelo Morador
# ─────────────────────────────────────────────────────────────
class MoradorViewSet(viewsets.ModelViewSet):
    queryset = Morador.objects.all().order_by('nome')
    serializer_class = MoradorSerializer
    permission_classes = get_viewset_permissions('MoradorViewSet')

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['email', 'unidade', 'is_proprietario', 'is_inquilino', 'pode_votar']
    search_fields = ['nome', 'email']
    ordering_fields = ['nome', 'email']

    # ✅ POST /api/moradores/{id}/aprovar/
    @action(detail=True, methods=['post'], url_path='aprovar')
    def aprovar_morador(self, request, pk=None):
        """Ativa o usuário vinculado ao morador."""
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
        Permite que um admin/síndico altere o campo 'pode_votar' de um morador.
        Body esperado: { "pode_votar": true/false }
        """
        morador = self.get_object()
        pode_votar = request.data.get('pode_votar')

        if pode_votar is None:
            return Response({'error': 'Campo "pode_votar" é obrigatório.'}, status=status.HTTP_400_BAD_REQUEST)

        morador.pode_votar = pode_votar
        morador.save()
        return Response({
            'status': 'Atualização de voto realizada com sucesso',
            'morador': morador.nome,
            'pode_votar': morador.pode_votar
        }, status=status.HTTP_200_OK)
